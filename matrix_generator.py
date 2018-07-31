import csv,globalparameter,re,itertools,jobtitleextractor


def matrix_generator_test(folderpath, non_folderpath, jobtitle_name,job_title,ratio,reader,reader1,writer,indexnumber):
    name = jobtitle_name
    content1 = []
    content2 = []
    # outputfile.close()
def matrix_generator_train(folderpath, non_folderpath, jobtitle_name,job_title,ratio,reader,reader1,writer,indexnumber):
    name = jobtitle_name
    content1 = []
    content2 = []
    job_title_list  = jobtitleextractor.extract_jobtitle(indexnumber)
    # , open('output.csv','w') as outputfile
    regex_year = re.compile('((\d+)\s+years?)')

        # writer = csv.DictWriter(outputfile)
    j = 0
    have1 = 0
    donthave = 0
    i = 0
    for row in itertools.islice(reader,0,500):
        for k in range(len(job_title_list)):
            if job_title_list[k] in row[3]:
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
                content1.append(0)
                content2.append(content1)
                donthave = donthave + 1
                content1 = []
            j = j + 1
            if job_title_list[k] in row[9]:
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
                content1.append(0)
                content2.append(content1)
                donthave = donthave + 1
                content1 = []
            j = j + 1
            if job_title_list[k] in row[15]:
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
                content1.append(0)
                content2.append(content1)
                donthave = donthave + 1
                content1 = []
            j = j + 1
            if job_title_list[k] in row[21]:
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
                content1.append(0)
                content2.append(content1)
                donthave = donthave + 1
                content1 = []
            j = j + 1
            if job_title_list[k] in row[27]:
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
                content1.append(0)
                content2.append(content1)
                donthave = donthave + 1
                content1 = []
            j = j + 1
            if job_title_list[k] in row[33]:
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
                content1.append(0)
                content2.append(content1)
                donthave = donthave + 1
                content1 = []
            j = j + 1
            if job_title_list[k] in row[39]:
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
                content1.append(0)
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

    for row in itertools.islice(reader1,0,500):
        for k in range(len(job_title_list)):
            if job_title_list[k] in row[3]:
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
                content1.append(0)
                content2.append(content1)
                donthave = donthave + 1
                content1 = []
            j = j + 1
            if job_title_list[k] in row[9]:
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
                content1.append(0)
                content2.append(content1)
                donthave = donthave + 1
                content1 = []
            j = j + 1
            if job_title_list[k] in row[15]:
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
                content1.append(0)
                content2.append(content1)
                donthave = donthave + 1
                content1 = []
            j = j + 1
            if job_title_list[k] in row[21]:
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
                content1.append(0)
                content2.append(content1)
                donthave = donthave + 1
                content1 = []
            j = j + 1
            if job_title_list[k] in row[27]:
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
                content1.append(0)
                content2.append(content1)
                donthave = donthave + 1
                content1 = []
            j = j + 1
            if job_title_list[k] in row[33]:
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
                content1.append(0)
                content2.append(content1)
                donthave = donthave + 1
                content1 = []
            j = j + 1
            if job_title_list[k] in row[39]:
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
                content1.append(0)
                content2.append(content1)
                donthave = donthave + 1
                content1 = []
            writer.writerows(content2)
            content2 = []
        # i = i + 1
    sparsityrate = float(have1) / float(donthave)
    print(jobtitle_name+" sparsity of train: %.4f" % sparsityrate)

    # outputfile.close()