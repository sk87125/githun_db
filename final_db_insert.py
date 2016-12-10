#!/usr/bin/python
import json
import pickledb

C_id = 1
#dict2 = {}
dict = {}
dict2 = {}

#Please try to create the youtube table structure first



db = pickledb.load('youtube.db', True) 
file = open('youtube.gais')
for line in file:
	#print line
	data_String = line.lstrip( '@' );	
	db.dcreate(C_id)
	if data_String != '\n':
		data_list = data_String.split(':')
		key_String = data_list[0]		
		value_String = data_list[1]		
		value_String=value_String.rstrip( '\n' );
		#print key_String		
		#print value_String		
		youtube_line = (key_String,value_String}
		print youtube_line
		#dict.update(youtube_line)
		db.dadd(C_id,key_String,value_String)
		#db.set(key_String, value_String) 
		if key_String=="_uid":
			#add_dict2 = {C_id:dict}
			C_id = C_id+1
			#print dict
			print '\n\n\n\n\n'			
			#dict2.update(add_dict2)
	
	
print dict2
file.close()
db.dump()
	
#db_string = input_string.split()
"""if db_string[0] == "exit":
	break
if db_string[0] == "INSERT":	
	print "Insrt success!!"
	print db_string
	key_String = db_string[3].lstrip( '(' );
	key_String = key_String.rstrip( ')' );
	key_list = key_String.split(',')
	print key_list
		
		
		split1 = x.split(' ')
		split2 = split1[3].split(',')
		split3 = split1[5].split(',')

		for i in range(0,len(split2)):
			add_dict = {split2[i]:split3[i]}
			dict.update(add_dict)
		
	add_dict2 = {C_id:dict}
	C_id += 1
	dict2.update(add_dict2)
	print (dict2)
	
	jsObj = json.dumps(dict2)  
	  
	fileObject = open('db.json', 'w')  
	fileObject.write(jsObj)  
	fileObject.close()  """