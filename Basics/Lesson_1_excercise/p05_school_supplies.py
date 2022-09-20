#Read Input
pencils_packs_cnt = int(input())
markers_packs_cnt = int(input())
clean_agent_liters = int(input())
discount = int(input()) / 100

#Process Input

pencils_price =  pencils_packs_cnt * 5.8
markers_price = markers_packs_cnt * 7.2
clean_agent_price = clean_agent_liters * 1.2

total_price = (pencils_price+markers_price+clean_agent_price) - (pencils_price+markers_price+clean_agent_price) * discount


#Print Output

print(total_price)