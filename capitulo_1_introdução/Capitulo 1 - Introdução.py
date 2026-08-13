#Capitulo 1 - Introdução
from collections import Counter
from collections import defaultdict
import matplotlib.pyplot as plt

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]

friendship_pairs = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),
                    (4,5),(5,6),(5,7),(6,8),(7,8),(8,9),]

friendships = {user["id"]: [] for user in users}

for i, j in friendship_pairs:
    friendships[i].append(j) # Add j como amigo do usuário i
    friendships[j].append(i) # Add i como amigo do usuário j

#Qual o número médio de conexões?
def number_of_friends(user):
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users)
print("Total de conexões:", total_connections)

num_users = len(users)
print("Número de usuários:", num_users)
avg_connections = total_connections / num_users 
print("Média de conexões:", avg_connections)

# Cria uma lista (user_id, número_de_amigos)
number_of_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

# ordena a lista em ordem decrescente
number_of_friends_by_id.sort(key = lambda id_and_friends: id_and_friends[1], reverse=True)

# Cientistas que talvez você conheça
# foaf significa amigo de um amigo
def foaf_ids_bad(user):
    return [foaf_id 
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]

print(friendships[0])
print(friendships[1])
print(friendships[2]) 

# conta quantos amigos em comum há
def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id
        and foaf_id not in friendships[user_id])

print(friends_of_friends(users[3]))

# lista com os interesses de cada usuário
interests = [
    (0, "hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"), (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"), (1, "Postgres"),
    (2, "Python"), (2, "scikit-learn"), (2, "scipy"), (2, "numpy"), (2, "statsmodels"), (2, "pandas"), 
    (3, "R"), (3, "Python"), (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decisions trees"), (4, "libsvm"),
    (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"), (5, "Haskell"), (5, "programming languages"),
    (6, "statistics"), (6, "probability"), (6, "mathematics"), (6, "theory"), 
    (7, "machine learning"), (7, "scikit-learn"), (7, "mahout"), (7, "neural networks"),
    (8, "neural networks"), (8, "deep learning"), (8, "Big Data"), (8, "artificial intelligence"),
    (9, "Hadoop"), (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

# retorna os usuários com o interesse alvo em comum
def data_sciebtists_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]

users_with_interest = data_sciebtists_who_like("Big Data")
print(f"Usuário que gostam de Big Data: {[users[id] for id in users_with_interest]}")

# Busca com índices
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

def most_commom_interests_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    )

print(f"Usuários com interesse em comum com '0 - Hero': {most_commom_interests_with(users[0])}")

print("\n")

# Salários e Experiência
print("Salários e Experiências")
print("\n")


salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

x = [ponto[0] for ponto in salaries_and_tenures]
y = [ponto[1] for ponto in salaries_and_tenures]

plt.scatter(y, x)
plt.xlabel("Anos de Experiência")
plt.ylabel("Salário")
plt.title("Salário por Anos de Experiência")
#plt.show()

salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

print(f"Média de salários por experiência {average_salary_by_tenure}")

def tenure_bucket(tenure):
    if tenure < 2:
        return "Menos que 2 anos de experiência"
    elif tenure < 5:
        return "Entre 2 e 5 anos de experiência"
    else:
        return "Mais de 5 anos de experiência"
    
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}    

print(average_salary_by_bucket)

print("\n")

#Contas a pagar
print("Contas a pagar")
print("\n")

user_paid_or_unpaid = [
    (0.7, "paid"), (1.9, "unpaid"), (2.5, "paid"), (4.2, "unpaid"),
    (6, "unpaid"), (6.5, "unpaid"), (7.5, "unpaid"), (8.1, "unpaid"),
    (8.7, "paid"), (10.0, "paid")
]

def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "Paid"
    elif years_experience < 8.5:
        return "Unpaid"
    else:
        return "Paid"

for years_experience, paid_or_unpaid in user_paid_or_unpaid:
    prediction = predict_paid_or_unpaid(years_experience)
    print(f"Years of Experience: {years_experience}, Actual: {paid_or_unpaid}, Predicted: {prediction}")

print("\n")

# Tópicos de interesse
print("Tópicos de interesse")
print("\n")

words_and_counts = Counter(word
                           for user, interest in interests
                           for word in interest.lower().split())

for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)
