import csv,globalparameter,re,itertools


def matrix_generator_test(folderpath, non_folderpath, jobtitle_name,job_title,ratio,reader,reader1,writer):
    name = jobtitle_name
    content1 = []
    content2 = []
    # , open('output.csv','w') as outputfile

    # writer = csv.DictWriter(outputfile)
    j = 0
    have1 = 0
    donthave = 0
    i = 0
    list1 = [9,15,21,27,33,39]
    for row in itertools.islice(reader,0,250):
        if name in row[3]:
            content1.append(row[0])
            content1.append(3)
            content1.append(-1)
            content2.append(content1)
            have1 = have1 + 1
            content1 = []
        else:
            content1.append(row[0])
            content1.append(3)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        j = j + 1
        if name in row[9]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[12]):
                if int(regex_year.findall(row[12])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(9)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(9)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(9)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(9)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        j = j + 1
        if name in row[15]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[18]):
                if int(regex_year.findall(row[18])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(15)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(15)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(15)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(15)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        j = j + 1
        if name in row[21]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[24]):
                if int(regex_year.findall(row[24])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(21)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(21)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(21)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(21)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        j = j + 1
        if name in row[27]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[30]):
                if int(regex_year.findall(row[30])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(27)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(27)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(27)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(27)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        j = j + 1
        if name in row[33]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[36]):
                if int(regex_year.findall(row[36])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(33)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(33)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(33)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(33)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        j = j + 1
        if name in row[39]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[42]):
                if int(regex_year.findall(row[42])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(39)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(39)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(39)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(39)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        writer.writerows(content2)
        content2 = []

    j = 0
    i = 0
    # writer = csv.DictWriter(outputfile)
    list1 = [9, 15, 21, 27, 33, 39]

    for row in itertools.islice(reader1,0,250):
        if name in row[3]:
            content1.append(row[0])
            content1.append(3)
            content1.append(-1)
            content2.append(content1)
            have1 = have1 + 1
            content1 = []
        else:
            content1.append(row[0])
            content1.append(3)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        j = j + 1
        if name in row[9]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[12]):
                if int(regex_year.findall(row[12])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(9)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(9)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(9)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(9)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        j = j + 1
        if name in row[15]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[18]):
                if int(regex_year.findall(row[18])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(15)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(15)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(15)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(15)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        j = j + 1
        if name in row[21]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[24]):
                if int(regex_year.findall(row[24])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(21)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(21)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(21)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(21)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        j = j + 1
        if name in row[27]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[30]):
                if int(regex_year.findall(row[30])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(27)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(27)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(27)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(27)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        j = j + 1
        if name in row[33]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[36]):
                if int(regex_year.findall(row[36])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(33)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(33)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(33)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(33)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        j = j + 1
        if name in row[39]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[42]):
                if int(regex_year.findall(row[42])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(39)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(39)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(39)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(39)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        writer.writerows(content2)
        content2 = []

    sparsityrate = float(have1) / float(donthave)
    print("sparsity: %.4f" % sparsityrate)

    # outputfile.close()


    # outputfile.close()
def matrix_generator_train(folderpath, non_folderpath, jobtitle_name,job_title,ratio,reader,reader1,writer):
    name = jobtitle_name
    content1 = []
    content2 = []
    # , open('output.csv','w') as outputfile
    regex_year = re.compile('((\d+)\s+years?)')

        # writer = csv.DictWriter(outputfile)
    j = 0
    have1 = 0
    donthave = 0
    i = 0
    for row in itertools.islice(reader,250,500):
        if name in row[3]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[6]):
                if int(regex_year.findall(row[6])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(3)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(3)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(3)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(3)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        j = j + 1
        if name in row[9]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[12]):
                if int(regex_year.findall(row[12])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(9)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(9)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(9)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(9)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        j = j + 1
        if name in row[15]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[18]):
                if int(regex_year.findall(row[18])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(15)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(15)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(15)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(15)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        j = j + 1
        if name in row[21]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[24]):
                if int(regex_year.findall(row[24])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(21)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(21)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(21)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(21)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        j = j + 1
        if name in row[27]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[30]):
                if int(regex_year.findall(row[30])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(27)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(27)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(27)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(27)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        j = j + 1
        if name in row[33]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[36]):
                if int(regex_year.findall(row[36])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(33)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(33)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(33)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(33)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        j = j + 1
        if name in row[39]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[42]):
                if int(regex_year.findall(row[42])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(39)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(39)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(39)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(39)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        writer.writerows(content2)
        content2 = []
    # i = i + 1
    j = 0

    # writer = csv.DictWriter(outputfile)
    j = 0
    i = 0
    list1 = [9, 15, 21, 27, 33, 39]

    for row in itertools.islice(reader1,250,500):

        if name in row[3]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[6]):
                if int(regex_year.findall(row[6])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(3)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(3)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(3)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(3)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        j = j + 1
        if name in row[9]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[12]):
                if int(regex_year.findall(row[12])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(9)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(9)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(9)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(9)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        j = j + 1
        if name in row[15]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[18]):
                if int(regex_year.findall(row[18])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(15)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(15)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(15)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(15)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        j = j + 1
        if name in row[21]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[24]):
                if int(regex_year.findall(row[24])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(21)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(21)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(21)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(21)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        j = j + 1
        if name in row[27]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[30]):
                if int(regex_year.findall(row[30])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(27)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(27)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(27)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(27)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        j = j + 1
        if name in row[33]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[36]):
                if int(regex_year.findall(row[36])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(33)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(33)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(33)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(33)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        j = j + 1
        if name in row[39]:
            regex_year = re.compile('((\d+)\s+years?)')
            if regex_year.findall(row[42]):
                if int(regex_year.findall(row[42])[0][1])>=3:
                    content1.append(row[0])
                    content1.append(39)
                    content1.append(2)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
                else:
                    content1.append(row[0])
                    content1.append(39)
                    content1.append(1)
                    content2.append(content1)
                    have1 = have1 + 1
                    content1 = []
            else:
                content1.append(row[0])
                content1.append(39)
                content1.append(1)
                content2.append(content1)
                have1 = have1 + 1
                content1 = []
        else:
            content1.append(row[0])
            content1.append(39)
            content1.append(-1)
            content2.append(content1)
            donthave = donthave + 1
            content1 = []
        writer.writerows(content2)
        content2 = []
        # i = i + 1
    sparsityrate = float(have1) / float(donthave)
    print("sparsity of train: %.4f" % sparsityrate)

    # outputfile.close()