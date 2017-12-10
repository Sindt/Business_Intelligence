# Business_Intelligence
#### Gruppe: Kasper Olesen, Kasper Pontoppidan & Christian Sindt

## Assignment 1: Environment Setup and Introduction to Python
```ruby 
Vagrant.configure("2") do |config|
  config.vm.provider "docker" do |d|
    d.image = "foo/bar"
  end
end
```
### 1. List the all files that this program generates:
IN:
```python
import assignment_1
import os

assignment_1.run()

os.listdir()
```

Output:

    ['.ipynb_checkpoints',
     'Assignment 1.ipynb',
     'assignment_1.py',
     'prices.png',
     'price_list.csv',
     'price_list.txt',
     'README.md',
     '__pycache__']

New files: **'prices.png',
     'price_list.csv',
     'price_list.txt',**



### 2. Describe which types of files this program generates and attach the contents of each file together with its name to your solution:

**Type: .PNG
NAME: prices.png**

```python
with open('prices.png', 'rb') as f:
        
    pngdata = f.read()
    print(len(pngdata))
```
    21862
    
   
**Type: .CSV
NAME: price_list.csv**

```python
with open('price_list.csv', 'r') as f:
    pngdata = f.read()
    print(pngdata)
```

    street,city,price,sqm,price_per_sqm
    "Ved Volden 5, 5. TV",1425 København K,4000000,91,43956
    "Rådhusstræde 4C, 1",1466 København K,4895000,105,46619
    "Store Kongensgade 112A, 3",1264 København K,250000,135,1851
    "Amaliegade 13G, 2",1256 København K,7375000,98,75255
    "Borgergade 144, 3. TH",1300 København K,5825000,101,57673
    "Nørre Søgade 9A, 1. TH",1370 København K,1126250,107,10525
    "Wildersgade 22, ST",1408 København K,1556700,88,17689
    "Toldbodgade 10A, 1",1253 København K,3750000,184,20380
    "Andreas Bjørns Gade 4, 3. TH",1428 København K,1700000,54,31481
    "Sølvgade 15, 4. TH",1307 København K,4215000,81,52037
    "Linnésgade 16A, 1",1361 København K,6300000,155,40645
    "Store Kongensgade 63A, ST. 4",1264 København K,1780000,98,18163
    "Peder Skrams Gade 28, 2. TV",1054 København K,4080000,76,53684
    "Brobergsgade 14, 1. TV",1427 København K,2750000,50,55000
    "Sølvgade 13, 2. TV",1307 København K,3150000,73,43150
    "Ny Adelgade 9, 2. TH",1104 København K,1950000,70,27857
    "Lavendelstræde 9, 2. TV",1462 København K,1550000,66,23484
    "Åbenrå 10, 2. 5",1124 København K,1650000,70,23571
    "Grønnegade 31, 3. TV",1107 København K,1200000,49,24489
    "Badstuestræde 16, 2",1209 København K,2700000,97,27835
    "Nørre Voldgade 70, 4",1358 København K,1870000,99,18888
    "Fredericiagade 25, 5. 1",1310 København K,3150000,118,26694
    "Sølvgade 19, 2. MF",1307 København K,2425000,49,49489
    "David Balfours Gade 3, ST. TV",1402 København K,3100000,83,37349
    "Vimmelskaftet 36A, 3. TH",1161 København K,3695000,84,43988
    "Store Kongensgade 110C, 3. TV",1264 København K,3050000,118,25847
    "Andreas Bjørns Gade 10, 3. TV",1428 København K,2367000,53,44660
    "Grønnegade 31, 4",1107 København K,3950000,73,54109
    "Peder Skrams Gade 27, 3. TH",1054 København K,6250000,112,55803
    "Andreas Bjørns Gade 22, 3. TH",1428 København K,2900000,55,52727
    "Kronprinsessegade 10, 4. TV",1306 København K,4350000,101,43069
    "Bartholinsgade 11, 1. TV",1356 København K,841000,52,16173
    "Sankt Peders Stræde 17, 2",1453 København K,4125000,106,38915
    "Ved Volden 11, 4. TH",1425 København K,4900000,97,50515
    Luftmarinegade 38,1432 København K,2485131,137,18139
    "Gernersgade 5, ST. TV",1319 København K,1950000,37,52702
    "Ahlefeldtsgade 26, 4. TV",1359 København K,2115000,82,25792
    "Dronningens Tværgade 36, 4. 1",1302 København K,1785000,82,21768
    "Nikolajgade 20, 2. TV",1068 København K,3500000,92,38043
    "Strandgade 12, 3",1401 København K,7170000,228,31447
    "Store Kongensgade 90, 2. TH",1264 København K,7500000,158,47468
    "Gothersgade 147, 3. TV",1123 København K,3622500,68,53272
    

**Type: .TXT
NAME: price_list.txt**

```python
with open('price_list.txt', 'r') as f:
    pngdata = f.read()
    print(pngdata)
```

      * Ved Volden 5, 5. TV; 1425 København K	4000000	91
      * Rådhusstræde 4C, 1; 1466 København K	4895000	105
      * Store Kongensgade 112A, 3; 1264 København K	250000	135
      * Amaliegade 13G, 2; 1256 København K	7375000	98
      * Borgergade 144, 3. TH; 1300 København K	5825000	101
      * Nørre Søgade 9A, 1. TH; 1370 København K	1126250	107
      * Wildersgade 22, ST; 1408 København K	1556700	88
      * Toldbodgade 10A, 1; 1253 København K	3750000	184
      * Andreas Bjørns Gade 4, 3. TH; 1428 København K	1700000	54
      * Sølvgade 15, 4. TH; 1307 København K	4215000	81
      * Linnésgade 16A, 1; 1361 København K	6300000	155
      * Store Kongensgade 63A, ST. 4; 1264 København K	1780000	98
      * Peder Skrams Gade 28, 2. TV; 1054 København K	4080000	76
      * Brobergsgade 14, 1. TV; 1427 København K	2750000	50
      * Sølvgade 13, 2. TV; 1307 København K	3150000	73
      * Ny Adelgade 9, 2. TH; 1104 København K	1950000	70
      * Lavendelstræde 9, 2. TV; 1462 København K	1550000	66
      * Åbenrå 10, 2. 5; 1124 København K	1650000	70
      * Grønnegade 31, 3. TV; 1107 København K	1200000	49
      * Badstuestræde 16, 2; 1209 København K	2700000	97
      * Nørre Voldgade 70, 4; 1358 København K	1870000	99
      * Fredericiagade 25, 5. 1; 1310 København K	3150000	118
      * Sølvgade 19, 2. MF; 1307 København K	2425000	49
      * David Balfours Gade 3, ST. TV; 1402 København K	3100000	83
      * Vimmelskaftet 36A, 3. TH; 1161 København K	3695000	84
      * Store Kongensgade 110C, 3. TV; 1264 København K	3050000	118
      * Andreas Bjørns Gade 10, 3. TV; 1428 København K	2367000	53
      * Grønnegade 31, 4; 1107 København K	3950000	73
      * Peder Skrams Gade 27, 3. TH; 1054 København K	6250000	112
      * Andreas Bjørns Gade 22, 3. TH; 1428 København K	2900000	55
      * Kronprinsessegade 10, 4. TV; 1306 København K	4350000	101
      * Bartholinsgade 11, 1. TV; 1356 København K	841000	52
      * Sankt Peders Stræde 17, 2; 1453 København K	4125000	106
      * Ved Volden 11, 4. TH; 1425 København K	4900000	97
      * Luftmarinegade 38; 1432 København K	2485131	137
      * Gernersgade 5, ST. TV; 1319 København K	1950000	37
      * Ahlefeldtsgade 26, 4. TV; 1359 København K	2115000	82
      * Dronningens Tværgade 36, 4. 1; 1302 København K	1785000	82
      * Nikolajgade 20, 2. TV; 1068 København K	3500000	92
      * Strandgade 12, 3; 1401 København K	7170000	228
      * Store Kongensgade 90, 2. TH; 1264 København K	7500000	158
      * Gothersgade 147, 3. TV; 1123 København K	3622500	68
    



### 3. What is the output of this program?


```python
assignment_1.run()
```
Output:
    3307228.119047619
    
<p>Output'et er en udregnet gennemsnitspris af de solgte boliger i KBH K</p>




### 4. Describe in natural language and line-by-line what the program is doing. Describe also for each line what the Python code expresses.

```python
def run():
1:    file_url = 'https://raw.githubusercontent.com/datsoftlyngby/' \
               'soft2017fall-business-intelligence-teaching-material/master/' \
               'assignments/assignment_1/price_list.txt'
2:  txt_file_name = os.path.basename(file_url)
3:  txt_path = os.path.join('./', txt_file_name)
4:  download_txt(file_url, txt_path)
5:  csv_file_name = 'price_list.csv'
6:  csv_path = os.path.join(os.getcwd(), csv_file_name)
7:  generate_csv(txt_path, csv_path)
8:  data = read_prices(csv_path)
9:  avg_price = compute_avg_price(data)
10: print(avg_price)
11: generate_plot(data)
    ```

1: Assignment af variable, som indeholder URL til price_list.txt fil.
2: Metode kald, som bruges til at hente navnet på filen, og assigne det i en variable.
3: Metode kald, for at lave en sti til filen som blev gemt i variablen. Dette bliver assignet til en ny variable.
4: Kald af metode download_txt(), som tager to argumenter. Metoden downloader filen fra url'en og gemmer den i stien.
5: Assignment af variable.
6: Samme som nr. 3, denne gang er det stien til "current working directory", og navnet på csv. filen.
7: Kald af metode generate_cvs(), som tager to argumenter. Metoden genere en csv fil dannet af indholdet af txt filen.
8: Kald af metode, read_price som tager et argument. Metoden læser boligpriserne fra csv filen og assigner dem
   i en data variable.
9: Kald af metode, avg_price som tager et argument. Metoden udregner gns. pris ved hjælp af data variablen,
   som indeholder priserne.
10: Udskriver gns. pris.
11: Kald af metode generate_plot, som taget et argument. Metoden genere en png fil som bruges til graf over
    gns. priserne.



