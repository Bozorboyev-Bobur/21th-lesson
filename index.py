# with open('./data.txt', 'r') as rf:
#     lines = rf.readlines()
#     users = []
#     for line in lines:
#         list = line.strip().split(';')
#         user = {
#             'fullName': list[0],
#             'birthDate': list[1],
#             'age': int(list[2]),
#             'sex': list[3]
#         }
#         users.append(user)
#     print(users)

# print(isinstance(True, str))
# print(type(1) == int)


# with open('./data.txt', 'r') as rf:
#     lines = rf.readlines()
#     numbers = []
#     for line in lines:
#         list = line.strip().split(';')
#         if len(list) == 1:
#             numbers.append(list[0])
#     print(numbers)


# with open('./data.txt', 'r') as rf:
#     numbers = []
#     for line in rf:
#         line = line.strip()
#         if line.isdigit():
#             numbers.append(int(line))
#     print(numbers)

# with open('./data.txt', 'r') as rf:
#     numbers = []
#     for line in rf:
#         line = line.strip()
#         if line.isdigit():
#             numbers.append(int(line))
#     print(numbers)


# with open('./data.txt', 'r') as rf:
#     numbers = []
#     for line in rf:
#         line = line.strip()
#         if line.isdigit():
#             numbers.append(int(line))
#     print(numbers)