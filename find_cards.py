import os
import shutil



import struct
from PIL import Image
import os.path


def check_if_high_res(files):
    high_res = False
    for file in files:
        img = Image.open(file)
        if (img.size[0]==3288):
            high_res = True
    return high_res


def find_all(name, path):
    result = []


    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))

    return result

path = '.\cards\\'

def get_images(deck_name, card_list):
    print('heres the deck name', deck_name)
    try:
        os.makedirs('.\decks\\'+deck_name)
    except:
        pass
    output = ''
    print("heres the card list")
    card_list = eval(card_list)
    for line in card_list:

        card_name = line.strip()
        try:
            #qty, name = card_name.split('\t',1)
            name = card_name
            qty = 1
        except:
            continue
        formatted_name = None
        for count in range(int(qty)):
            card_dict = {
                         'high_res': [],
                         'low_res': []
                        }

            name = name.replace("\'",'_')
            name = name.replace('The ', 'the ')
            name = name.replace('For ', 'for ')
            name = name.replace('To ', 'to ')
            name = name.replace('Of ', 'of ')
            if ".png" not in name:
                name = name + '.png'

            cards_found = find_all(name, path)


            #print(name,end='\t\t')

            if formatted_name is None:
                formatted_name = name.replace(".png", ' %s %s %s.png')

            for card_found in cards_found:
                img = Image.open(card_found)
                if img.size[0]==3288:
                    card_dict['high_res'].append(card_found)
                else:
                    card_dict['low_res'].append(card_found)
            '''
            if len(card_dict['low_res'])==2 and len(card_dict['high_res'])==0:
                print('found %s low res - choosing one' % len(card_dict['low_res']))
                for i in range(len(card_dict['low_res'])):

                    shutil.copyfile(card_dict['low_res'][i], '.\decks\\' + formatted_name % ('low_res', i, count))
                    break
            '''
            if len(card_dict['high_res'])>0:
                print(' = found %s high res' % len(card_dict['high_res']))
                output = output + card_name + '   found %s high res\n' % len(card_dict['high_res'])
                for i in range(len(card_dict['high_res'])):
                    shutil.copyfile(card_dict['high_res'][i], '.\decks\\'+deck_name+'\\' + formatted_name % ('high_res', i, count))

            elif len(card_dict['low_res'])>0:
                print(' = found %s low res' % len(card_dict['low_res']))
                output = output + card_name + '   found %s low res\n' % len(card_dict['low_res'])
                for i in range(len(card_dict['low_res'])):
                    shutil.copyfile(card_dict['low_res'][i], '.\decks\\'+deck_name+'\\' + formatted_name % ('low_res', i, count))

            else:
                print(' = COULD NOT FIND CARD')
                output = output + card_name + '   COULD NOT FIND CARD\n'
    
    shutil.make_archive('.\decks\\'+deck_name, 'zip', '.\decks\\'+deck_name)

    dir = '.\decks\\'+deck_name
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

    os.rmdir(os.path.join(dir))
 
    return output