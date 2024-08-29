import argparse
from collections import Counter
from pprint import pprint
import pathlib

ID, FORM, LEMMA, UPOS, XPOS, FEATS, HEAD, DEPREL, DEPS, MISC = range(10)


def vote_upos(upos):
    c = Counter(upos)
    k, v = c.most_common(1)[0]  # Most common UPOS
    return k, v


def analyze_data(upos_votes, total_lines):
    agreed = [tuple(upos) for upos, count in upos_votes if count > 1]  # Includes also cases where one disagrees with the other two.
    dispersed_groups = [tuple(sorted(upos)) for upos, count in upos_votes if count == 1]  # sort to normalize ordering

    most_agreed = Counter(agreed).most_common(30)
    most_dispersed = Counter(dispersed_groups).most_common(30)

    agreed_proportion = sum(count for _, count in most_agreed) / total_lines
    dispersed_proportion = sum(count for _, count in most_dispersed) / total_lines

    most_agreed_percentages = [
        (tag, count / total_lines * 100) for tag, count in most_agreed
    ]
    most_dispersed_percentages = [
        (tags, count / total_lines * 100) for tags, count in most_dispersed
    ]

    return (
        most_agreed,
        most_dispersed,
        agreed_proportion,
        dispersed_proportion,
        most_agreed_percentages,
        most_dispersed_percentages,
    )


def main(args):
    files = [open(fname, "rt", encoding="utf-8") for fname in args.predicted_files]

    wdir = pathlib.Path('Results/analyse')
    wdir.mkdir(parents=True, exist_ok=True)

    upos_votes = []
    total_lines = 0
    incorrect_dispersed = []

    for lines in zip(*files):
        lines = [line.strip() for line in lines]
        if not lines[0] or lines[0].startswith("#"):
            continue
        cols = [line.split("\t") for line in lines]
        if "-" in cols[0][ID]:
            continue

        upos = [c[UPOS] for c in cols]
        voted_upos, vote_count = vote_upos(upos)
        upos_votes.append((upos, vote_count))
        total_lines += 1

        if vote_count == 1:  # All UPOS tags are unique
            correct_upos = cols[0][UPOS]  # Assume the first file is the ground truth
            # BUG?: We need to compare to gold standard? 
            # At least in vote.py vote_upos is always from the first file, 
            # i.e. voted_upos == correct_upos always.
            if voted_upos != correct_upos:
                incorrect_dispersed.append((cols[0][FORM], upos, correct_upos))

    (
        most_agreed,
        most_dispersed,
        agreed_proportion,
        dispersed_proportion,
        most_agreed_percentages,
        most_dispersed_percentages,
    ) = analyze_data(upos_votes, total_lines)

    with open(args.output, "wt", encoding="utf-8") as f:
        f.write("Most Agreed UPOS Tags (with counts and percentages):\n")
        for tag, count in most_agreed:
            percentage = count / total_lines * 100
            f.write(f"{tag}: {count} ({percentage:.2f}%)\n")
        f.write(f"Proportion of Most Agreed UPOS Tags: {agreed_proportion:.2%}\n\n")

        f.write("Most Dispersed UPOS Tags (with counts and percentages):\n")
        for tags, count in most_dispersed:
            percentage = count / total_lines * 100
            f.write(f"{', '.join(tags)}: {count} ({percentage:.2f}%)\n")
        f.write(
            f"Proportion of Most Dispersed UPOS Tags: {dispersed_proportion:.2%}\n\n"
        )

        f.write("Cases where predictions are dispersed and incorrect:\n")
        for form, upos, correct_upos in incorrect_dispersed:
            f.write(
                f"Word: {form}\nPredictions: {', '.join(upos)}\nCorrect UPOS: {correct_upos}\n\n"
            )

    # with open(wdir/"incorrect_dispersed", 'w', encoding="utf8") as g:
    #     pprint(incorrect_dispersed, g)
    # with open(wdir/"most_agreed", 'w', encoding="utf8") as g:
    #     pprint(most_agreed, g)

    print(f"Analysis complete. Results written to {args.output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze UPOS voting results")
    parser.add_argument("predicted_files", nargs="+", help="Files to use")
    parser.add_argument("--output", type=str, required=True, help="Output file")
    args = parser.parse_args()

    main(args)
