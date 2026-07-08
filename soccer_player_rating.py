squad=[]
def add_player(name,position,match_ratings):
    return {'name':name,'position':position,'match_ratings':match_ratings}
squad.append(add_player(name='bruno fernandes',position='middlefielder',match_ratings=[10,9,8,7]))
squad.append(add_player(name='benjamin sesko',position='striker',match_ratings=[5,4,3,6]))
squad.append(add_player(name='diogo',position='goal keeper',match_ratings=[2,3,6,8]))

print('squad list')

def display(squad):
    for n in(squad):
        print(n['name'],n['position'])
display(squad)

def best_player(squad):
    top_name = ''
    top_avg = 0
    for best in squad:
        avg = sum(best['match_ratings']) / len(best['match_ratings'])
        if avg > top_avg:
            top_avg = avg
            top_name = best['name']
    return f' top player name:{top_name}, top player rating:{top_avg}'

print(best_player(squad))
        

        
        
        


    

     



