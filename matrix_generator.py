import csv, globalparameter

def generate_train_matrix(folderpath, jobtitle_path_list):
    List1 = []
    with open('company_name.csv', 'rb') as csvfile1:
        reader = csv.DictReader(csvfile1)
        i = 0
        for i, row in enumerate(reader):
            if i < 30:
                List1.append(row['companynames'])
            i = i + 1

    content1 = []
    content2 = []
    content3 = []
    # , open('output.csv','w') as outputfile
    with open(folderpath +'/' + jobtitle_path_list +globalparameter.output_file_root, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        # writer = csv.DictWriter(outputfile)
        j = 0
        have1 = 0
        donthave = 0
        i = 0
        writer = csv.writer(open('test7.csv', 'w'))
        for i, row in enumerate(reader):
            if i < 3566:
                print(i)
                for j in range(len(List1)):
                    if List1[j] in row['org_summary']:
                        content1.append(row['id'])
                        content1.append(j + 1)
                        content1.append(1)
                        content2.append(content1)
                        have1 = have1 + 1
                        content1 = []
                    elif List1[j] in row['past_job_org_summary1']:
                        content1.append(row['id'])
                        content1.append(j + 1)
                        content1.append(1)
                        content2.append(content1)
                        have1 = have1 + 1
                        content1 = []
                    elif List1[j] in row['past_job_org_summary2']:
                        content1.append(row['id'])
                        content1.append(j + 1)
                        content1.append(1)
                        content2.append(content1)
                        have1 = have1 + 1
                        content1 = []
                    elif List1[j] in row['past_job_org_summary3']:
                        content1.append(row['id'])
                        content1.append(j + 1)
                        content1.append(1)
                        content2.append(content1)
                        have1 = have1 + 1
                        content1 = []
                    elif List1[j] in row['past_job_org_summary4']:
                        content1.append(row['id'])
                        content1.append(j + 1)
                        content1.append(1)
                        content2.append(content1)
                        have1 = have1 + 1
                        content1 = []
                    elif List1[j] in row['past_job_org_summary5']:
                        content1.append(row['id'])
                        content1.append(j + 1)
                        content1.append(1)
                        content2.append(content1)
                        have1 = have1 + 1
                        content1 = []
                    elif List1[j] in row['past_job_org_summary6']:
                        content1.append(row['id'])
                        content1.append(j + 1)
                        content1.append(1)
                        content2.append(content1)
                        have1 = have1 + 1
                        content1 = []
                    else:
                        content1.append(row['id'])
                        content1.append(j + 1)
                        content1.append(-1)
                        content2.append(content1)
                        donthave = donthave + 1
                        content1 = []

                writer.writerows(content2)
                content2 = []
            i = i + 1
            j = j + 1

    sparsityrate = float(have1) / float(donthave)
    print("sparsity: %.4f" % sparsityrate)
    csvfile.close()
    csvfile1.close()
    # outputfile.close()


def generate_test_matrix(folderpath,jobtitle_path_list):
    List1 = []
    with open('company_name.csv', 'rb') as csvfile1:
        reader = csv.DictReader(csvfile1)
        i = 0
        for i, row in enumerate(reader):
            if i < 30:
                List1.append(row['companynames'])
            i = i + 1

    content1 = []
    content2 = []
    content3 = []
    # , open('output.csv','w') as outputfile
    with open(folderpath +'/' + jobtitle_path_list +globalparameter.output_file_root, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        # writer = csv.DictWriter(outputfile)
        j = 0
        have1 = 0
        donthave = 0
        i = 0
        writer = csv.writer(open('test7.csv', 'w'))
        for i, row in enumerate(reader):
            if i < 3566:
                print(i)
                for j in range(len(List1)):
                    if List1[j] in row['org_summary']:
                        content1.append(row['id'])
                        content1.append(j + 1)
                        content1.append(1)
                        content2.append(content1)
                        have1 = have1 + 1
                        content1 = []
                    elif List1[j] in row['past_job_org_summary1']:
                        content1.append(row['id'])
                        content1.append(j + 1)
                        content1.append(1)
                        content2.append(content1)
                        have1 = have1 + 1
                        content1 = []
                    elif List1[j] in row['past_job_org_summary2']:
                        content1.append(row['id'])
                        content1.append(j + 1)
                        content1.append(1)
                        content2.append(content1)
                        have1 = have1 + 1
                        content1 = []
                    elif List1[j] in row['past_job_org_summary3']:
                        content1.append(row['id'])
                        content1.append(j + 1)
                        content1.append(1)
                        content2.append(content1)
                        have1 = have1 + 1
                        content1 = []
                    elif List1[j] in row['past_job_org_summary4']:
                        content1.append(row['id'])
                        content1.append(j + 1)
                        content1.append(1)
                        content2.append(content1)
                        have1 = have1 + 1
                        content1 = []
                    elif List1[j] in row['past_job_org_summary5']:
                        content1.append(row['id'])
                        content1.append(j + 1)
                        content1.append(1)
                        content2.append(content1)
                        have1 = have1 + 1
                        content1 = []
                    elif List1[j] in row['past_job_org_summary6']:
                        content1.append(row['id'])
                        content1.append(j + 1)
                        content1.append(1)
                        content2.append(content1)
                        have1 = have1 + 1
                        content1 = []
                    else:
                        content1.append(row['id'])
                        content1.append(j + 1)
                        content1.append(-1)
                        content2.append(content1)
                        donthave = donthave + 1
                        content1 = []

                writer.writerows(content2)
                content2 = []
            i = i + 1
            j = j + 1

    sparsityrate = float(have1) / float(donthave)
    print("sparsity: %.4f" % sparsityrate)
    csvfile.close()
    csvfile1.close()
