from bs4 import BeautifulSoup
import requests
import statistics

url = "https://drive.google.com/u/0/uc?id=1nf9WMDjZWIUnlnKyz7qomEYDdtWfW1Uf&export=download"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html5lib')

datas = soup.find_all("td")
data = []
for i in range(1,10,2):
    data.append(datas[i].string)

frequency = {}

for datum in data:
    unstripped = datum.split(",")
    for j in range(len(unstripped)):
        unstripped[j] = unstripped[j].strip()
        match unstripped[j]:
            case "GREEN":
                frequency["green"] = frequency.get("green", 0) + 1
            case "YELLOW":
                frequency["yellow"] = frequency.get("yellow", 0) + 1
            case "BROWN":
                frequency["brown"] = frequency.get("brown", 0) + 1
            case "BLUE":
                frequency["blue"] = frequency.get("blue", 0) + 1
            case "PINK":
                frequency["pink"] = frequency.get("pink", 0) + 1
            case "ORANGE":
                frequency["orange"] = frequency.get("orange", 0) + 1
            case "RED":
                frequency["red"] = frequency.get("red", 0) + 1
            case "WHITE":
                frequency["white"] = frequency.get("white", 0) + 1
            case "ARSH":
                frequency["arsh"] = frequency.get("arsh", 0) + 1
            case "BLEW":
                frequency["blew"] = frequency.get("blew", 0) + 1
            case "CREAM":
                frequency["cream"] = frequency.get("cream", 0) + 1
            case "BLACK":
                frequency["black"] = frequency.get("black", 0) + 1
            case _:
                print("This is an unaccounted colour. There's a bug somewhere. Further action on this statistic is highly prone to error.")
print("                         MEAN")
mean = statistics.mean(frequency.values())
print("The mean of the categorical data(grouped) is the mean of their cummulative frequencies.")
print(f"Using the cummulative frequency table we have that mean = cummulative frequency / no. of ocurrences = {mean}.")
print("We can therefore infer from our frequency distribution that our mean colour is PINK and YELLOW.")


print("\n                       MODE")
mode_id = "green"
mode = frequency.get(mode_id)

for key,value in frequency.items():
    if value > mode:
        mode = value
        mode_id = key
print(f"The modal value of our frequency distribution is {mode} and our mode is {mode_id.upper()}.")

print("\n                       MEDIAN")
print("The median of our frequency distribution is 5.5 approx. 6 which is BROWN")

print("\n                       VARIANCE")
print(f"The variance of the frequency distribution is {statistics.variance(frequency.values())}")

print("\n                      PROBABILITY")
print(f"The probability of choosing a red colour at random is no. of red occureences / total no. of courrences = {frequency.get('red') / sum(frequency.values())}")

def recursive_search(array: list, search: int, idx = 0):
    if search == array[0]:
        return f"Found {search} at index {idx}"
    return recursive_search(array[1:], search, idx+1)


def sum_fibonacci():
    total_sum = 0
    first, second = 0, 1
    for i in range(2, 50):
        total_sum += first + second
        temp = second
        second = first + second
        first = temp
    return total_sum