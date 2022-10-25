value=list(map(int,input("Enter value: ").split(',')))#list(map(int,input("Enter value: ").split(','))) урывок с видео
#Value = value.split(',')
print(f'Maximum number: {max(value)}')
print(f'Minimum number: {min(value)}')
print(f'Sum number list: {sum(value)-min(value)-max(value)}')