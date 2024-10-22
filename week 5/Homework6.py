#Ödev-5.2:
#3.Enumerate methodunu araştırın ve aşağıdaki örneği enumerate methodu ile yapın.

        #for index in range(len(meyveler)):

            #print("{}. indexte bulunan meyve: {}".format(index,meyveler[index])

meyveler = ["erik", "elma", "muz", "çilek"]
for index, meyve in enumerate(meyveler):
    print("{}. indexte bulunan meyve: {}".format(index, meyve))