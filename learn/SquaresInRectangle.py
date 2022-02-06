# From: https://www.codewars.com/kata/rectangle-into-squares/python

def squares_in_rectangle(length, width):
    if length == width:
        return length

    rect_counts = []
    min_side = 1
    while min_side > 0:
        # print("DEBUG", length, width)
        if length < width:
            min_side = length
            width -= min_side
        else:
            min_side = width
            length -= min_side

        if min_side > 0:
            rect_counts.append(min_side)

    print(f"Input=[{length}, {width}] Result={rect_counts}")
    return rect_counts


# squares_in_rectangle(5, 5)  # None)
squares_in_rectangle(5, 3)  # [3, 2, 1, 1])
squares_in_rectangle(20, 14)  # [14, 6, 6, 2, 2, 2])
squares_in_rectangle(37, 14)  # [14, 14, 9, 5, 4, 1, 1, 1, 1])
