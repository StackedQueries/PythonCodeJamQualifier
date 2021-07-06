from typing import List, Any,Optional

def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """

    line_top = ["─", "┌", "┬", "┐"]
    line_middle = ["─", "├", "┼", "┤"]
    line_bottom = ["─", "└", "┴", "┘"]
    line_etc = [" ", "│", "│", "│"]

    def create_line(sections=List, line_types=List[Any], width=List[int], type=None) -> str:
        line = [line_types[1]]
        for c, cell in enumerate(sections):
            if type == "sep":
                line.append(''.join(line_types[0] for i in range(width[c])) + "─")
            elif len(str(cell)) >= 1:
                white_space = ''.join(" " for i in range(longest[c] - len(str(cell))))

                if centered:
                    extra_space = ""
                    white_space = ''.join(" " for i in range(int((longest[c] - len(str(cell)))/2)))
                    if (longest[c] - len(str(cell)))%2 != 0:
                        extra_space = " "

                    line.append(' ' + white_space +
                                str(cell) + white_space+extra_space)
                    #line.append(' ' + white_space[int(len(white_space) / 2):] +
                    #            str(cell) + white_space[:int(len(white_space) / 2)])
                else:
                    line.append(' ' + str(cell) + white_space)
            else:
                line.append(line_types[0])

                line.append(''.join(line_types[0] for i in range(width[c])))
            try:
                if sections[c + 1] or sections[c + 1] == None:
                    line.append(line_types[0] + line_types[2])
            except:
                if type == "sep":
                    line.append("─")
                else:
                    line.append(" ")

        line.append(line_types[3] + "\n")
        return "".join(line)

    table = None
    row_length = len(rows[0])
    longest = [0 for i in range(row_length)]  # set 0 in each Col

    # Find Longest in each  coloumn
    def find_longest():
        for r_count, row in enumerate(rows):

            if labels:
                for l_count, label in enumerate(labels):
                    if longest[l_count] < len(str(label)):
                        longest[l_count] = len(str(label))

            for e_count, ele in enumerate(row):
                if longest[e_count] < len(str(ele)):
                    longest[e_count] = len(str(ele))

    find_longest()

    table = []

    table.append(create_line(sections=longest, width=longest, line_types=line_top, type="sep"))

    if labels:

        table.append(create_line(sections=labels, width=longest, line_types=line_etc))

        table.append(create_line(sections=longest, width=longest, line_types=line_middle, type="sep"))

    x = list(map(lambda x: create_line(sections=x, width=longest, line_types=line_etc), rows))
    for i in x:
        table.append(i)

    table.append(
        create_line(sections=labels if labels == True else longest, width=longest, line_types=line_bottom, type="sep"))

    return "".join(table)
