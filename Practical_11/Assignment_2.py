import matplotlib.pyplot as plt

companies = ['Microsoft', 'Google', 'Amazon', 'IBM', 'Deloitte', 'Capgemini', 'ATOS Origin', 'Amdocs']
recruits = [120, 150, 100, 80, 90, 70, 60, 85]  # Example data

plt.bar(companies, recruits, color='skyblue')
plt.title("New Recruitments per Company")
plt.xlabel("Companies")
plt.ylabel("Number of Recruits")
plt.xticks(rotation=45)
plt.show()