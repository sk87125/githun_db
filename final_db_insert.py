#!/usr/bin/python
import json
import pickledb

C_id = 1
dict = {"id":' ',"title":' ',"published":' ',"content":' ',"category":' ',"duration":0,"favoriteCount":0,"$viewCount":0,"author":' ',"keyword":' ',"_uid":0}
add_dict2={}
dict2 = dict.copy()
#Please try to create the youtube table structure first



db = pickledb.load('youtube1.db', False) 
file = open('youtube_1.gais')

for line in file:
	data_String = line.lstrip( '@' );		
	#db.dcreate(C_id)
	if data_String != '\n':
		data_list = data_String.split(':')
		key_String = data_list[0]		
		value_String = data_list[1]		
		value_String=value_String.rstrip( '\n' );
		#print key_String		
		#print value_String		
		youtube_line = {key_String:value_String}
		#print youtube_line
		dict2[key_String] = value_String
		#db.dadd(C_id,youtube_line)
		#db.set(key_String, value_String) 
		if key_String=="_uid":
			add_dict = {C_id:dict2}			
			C_id = C_id+1
			if C_id % 20 == 0:
				jsObj = json.dumps(add_dict2) 
			print C_id
			print '\n\n\n\n\n'
			add_dict2.update(add_dict.copy())
			dict2 = dict.copy()
			if C_id % 10000 == 0:
				break;
			
			
	
print add_dict2
file.close()
jsObj = json.dumps(add_dict2)  

fileObject = open('youtube.db', 'w')  
fileObject.write(jsObj)  
fileObject.close()  
#db.dump()	
#db_string = input_string.split()
