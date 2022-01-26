import requests
from bs4 import BeautifulSoup

html_text = requests.get('https://www.mohfw.gov.in/').text
soup = BeautifulSoup(html_text, 'lxml')

#finding active cases

def active_covid():
    active = soup.find('li', class_ = 'bg-blue').text

    cases = []

    cases.append(active.split())
    active = cases[0][1]

    return active
#vaccine status

def vaccinations():
    vaccine_stats = []

    vaccine = soup.find('div', class_ = 'col-xs-8 site-stats-count sitetotal').text

    vaccine_stats.append(vaccine.split())
    new = vaccine_stats[0][4]
    new_vaccines = new[1:len(new)-1]
    current = vaccine_stats[0][3]
    return current, new_vaccines

#finding number of deaths 
def covid_deaths():
        
    deaths = []

    death_table = soup.find('li', class_ = 'bg-red').text

    deaths.append(death_table.split())

    new1 = deaths[0][2]
    inc = new1[1:len(new1)-1]
    change = deaths[0][1]

    return change, inc

#displaying all cases 

def all_cases():
    html_text = requests.get('https://www.mygov.in/covid-19').text
    soup = BeautifulSoup(html_text, 'lxml')
    block = soup.find('div', class_ = 'iblock t_case')
    count = block.find('span', class_ = 'icount').text
    return count

#statewise data

def statewise():
    s1 = []
    state_final = []
    html_text = requests.get('https://prsindia.org/covid-19/cases').text
    soup = BeautifulSoup(html_text, 'lxml')
    table = soup.find('table', class_ = 'table table-striped table-bordered')
    body = table.find('tbody')
    state_names = body.find_all('td')
    for i in state_names:
        a = i.text
        s1.append(a)
    i = 0
    state = []
    for j in s1:
        if i < 6:
            state.append(j)
            i = i + 1
        elif i == 6:
            state_final.append(state)
            state = []
            state.append(j)
            i = 0
            
    name = input("Enter State Name:")
    for i in range(len(state_final)):
        if state_final[i][1] == name:
            confirmed = state_final[i][2]
            active = state_final[i][3]
            cured = state_final[i][4]
            deaths = state_final[i][5]
            print(f"State: {name}\nTotal cases: {confirmed}\nActive cases: {active}\nCured: {cured}\nDeaths: {deaths}\n")
statewise()
