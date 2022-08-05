import json
from datetime import date


def write_json(data, filename='weight.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    file = 'weight.json'

    today = date.today()
    todayDate = today.strftime('%m/%d/%y')
    
    weight = input('Enter Weight: ')
    
    while True:
        time = input('morning or night (m or n): ')
    
        if time.lower() == 'm' or time.lower() == 'n':
            break
        else:
            print('Invalid entry. Try Again')

    with open(file, 'r+') as json_file:
        data = json.load(json_file)
        name_data = (data['track'])
    
        day = []
    
        for i in name_data:
            day.append(i['date'])
    
        if todayDate in i['date']:
            if time.lower() == 'm':
                if i["weight-morning"] == '':
                    pass
                else:
                    print('You already have weight tracked for today.')
                    print(f'Date: {i["date"]} | Morning: {i["weight-morning"]} | Night: {i["weight-night"]}')
    
                    while True:
                        edit = input('Would you like to edit your input? (y, n): ')
    
                        if edit.lower() == 'y' or edit.lower() == 'n':
    
                            if edit.lower() == 'y':
                                i['weight-morning'] = weight
                                write_json(data)
                                print(
                                    f'Date: {i["date"]} | Morning: {i["weight-morning"]} | Night: {i["weight-night"]} | Updated')
                                quit()
                            elif edit.lower() == 'n':
                                print('Re-run the program to add more data')
                                quit()
                        else:
                            pass
            elif time.lower() == 'n':
                if i["weight-night"] == '':
                    pass
                else:
                    print('You already have weight tracked for today.')
                    print(f'Date: {i["date"]} | Morning: {i["weight-morning"]} | Night: {i["weight-night"]}')
    
                    while True:
                        edit = input('Would you like to edit your input? (y, n): ')
    
                        if edit.lower() == 'y' or edit.lower() == 'n':
    
                            if edit.lower() == 'y':
                                i['weight-night'] = weight
                                write_json(data)
                                print(
                                    f'Date: {i["date"]} | Morning: {i["weight-morning"]} | Night: {i["weight-night"]} | Updated')
                                quit()
                            elif edit.lower() == 'n':
                                print('Re-run the program to add more data')
                                quit()
                        else:
                            pass
    
        else:
    
            if time.lower() == 'm':
                with open('weight.json') as json_file:
                    data = json.load(json_file)
                    temp = data['track']
                    y = {'date': str(today.strftime('%m/%d/%y')), 'weight-morning': str(weight), 'weight-night': ''}
                    temp.append(y)
                    write_json(data)
    
            elif time.lower() == 'n':
                with open('weight.json') as json_file:
                    data = json.load(json_file)
                    temp = data['track']
                    y = {'date': str(today.strftime('%m/%d/%y')), 'weight-morning': '', 'weight-night': str(weight)}
                    temp.append(y)
                    write_json(data)

if __name__ == '__main__':
    main()