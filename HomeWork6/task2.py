# def max_letter(line, let):
#     count = 0
#     max = 0
#     for c in line:
#         if c == let:
#             count += 1
#         else:
#             if count > max:
#                 max = count
#             count = 0
#     if count > max:
#             max = count
#     return max

res = ["ОРРОРОРООРРРО", "ООООООРРРОРОРРРРРРР", "ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР"]
for line in res:
    # print(max_letter(line, "Р"))
    print(max([len(i) for i in line.split("О") if i]))
