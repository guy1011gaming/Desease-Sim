# 🦠 Pandemic Sim
In this project, I try to model the trend of a pandemic using python.

## ❓ How it works
In the begining, there is a certain percentage of society which is already immune against the desease. Every person has a number of friends, which is generated using a normal distribution. On each day, everyone has a chance of being infected, by randomly generating how many friends a person might meet. If a person meets a infected person, there is a chance of infecting each other, which is dependent on the previously infected person's contagiousness. Reliant on this, the person might be infected or not. 

## → Parameters
- Population: Number of people living in society
- Starting immunnity percentage: The percentage of people which are already immune against the desease
- Initially infected: Amount of people who are infected initially
- Days of contagiousness: The number of days a person will stay contagiousnes for

## 🔮 Future Plans
- Implementation of Lockdown
- Implementation of Face Masks
- Visualisation with live graphs

## 🙏🏻 Inspiration
This project has been inspired by [towardsdatascience](https://towardsdatascience.com/simulating-the-pandemic-in-python-2aa8f7383b55). Thank you for your great article. 
