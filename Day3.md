# Day3

```python
for key in phonebook:
    print("1:",key, end=' ')
    print("2:",phonebook[key])

for menu, tel in phonebook.items():
    # for key, value
    print("3:",menu, tel)

for value in phonebook.values():
    print("4:",value)
for key in phonebook.keys():
    print("5:",key)
```

`1: 중국집 2: 02821                                                              
1: 초밥집 2: 031                                                                
1: 한식집 2: 052                                                                
1: 분식집 2: 121312                                                             
3: 중국집 02821                                                                 
3: 초밥집 031                                                                   
3: 한식집 052                                                                   
3: 분식집 121312                                                                
4: 02821                                                                        
4: 031                                                                          
4: 052                                                                          
4: 121312                                                                       
5: 중국집                                                                       
5: 초밥집                                                                       
5: 한식집                                                                       
5: 분식집                                                                       `