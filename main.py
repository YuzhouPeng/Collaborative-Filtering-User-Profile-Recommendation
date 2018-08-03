import matrix_generator, globalparameter, csv,matrix_generator_pastexp

if __name__ == '__main__':
    for i in range(6):
        reader = csv.reader(open(globalparameter.folderpath[i] + '/' + 'output_pos_for_dummy.csv', 'r'))
        reader1 = csv.reader(open(globalparameter.folderpath[i] + '/' + 'output_neg_for_dummy.csv', 'r'))
        writer = csv.writer(open(
            globalparameter.collaborative_filtering_path + '/test_output_cf_' + globalparameter.jobtitle_path_list[i] + '.csv',
            'w'))
        writer1 = csv.writer(open(
            globalparameter.collaborative_filtering_path + '/train_output_cf_' + globalparameter.jobtitle_path_list[i] + '.csv',
            'w'))
        matrix_generator.matrix_generator_train(
            globalparameter.folderpath[i] + '/' + 'output_pos_for_dummy.csv',
            globalparameter.folderpath[i] + '/' + 'output_neg_for_dummy.csv', globalparameter.jobtitle_list[i],
            globalparameter.jobtitle_path_list[i], 0.5, reader, reader1,writer1,i)
        # print('begin the test -------------------')
        # reader = csv.reader(open(globalparameter.folderpath[i] + '/' + 'output_pos_for_dummy.csv', 'r'))
        # reader1 = csv.reader(open(globalparameter.folderpath[i] + '/' + 'output_neg_for_dummy.csv', 'r'))
        # matrix_generator.matrix_generator_test(globalparameter.folderpath[i] + '/' + 'output_pos_for_dummy.csv',
        #                                        globalparameter.folderpath[i] + '/' + 'output_neg_for_dummy.csv',
        #                                        globalparameter.jobtitle_list[i],
        #                                        globalparameter.jobtitle_path_list[i], 0.5,reader,reader1,writer,i)

        # reader = csv.reader(open(globalparameter.folderpath[i] + '/' + 'output_pos_for_dummy.csv', 'r'))
        # reader1 = csv.reader(open(globalparameter.folderpath[i] + '/' + 'output_neg_for_dummy.csv', 'r'))
        # writer = csv.writer(open(
        #     globalparameter.collaborative_filtering_path + '/test_output_cf_' + globalparameter.jobtitle_path_list[i] + '.csv',
        #     'w'))
        # writer1 = csv.writer(open(
        #     globalparameter.collaborative_filtering_path + '/train_output_cf_' + globalparameter.jobtitle_path_list[i] + '.csv',
        #     'w'))
        #
        # matrix_generator_pastexp.matrix_generator_train(
        #     globalparameter.folderpath[i] + '/' + 'output_pos_for_dummy.csv',
        #     globalparameter.folderpath[i] + '/' + 'output_neg_for_dummy.csv', globalparameter.jobtitle_list[i],
        #     globalparameter.jobtitle_path_list[i], 0.5, reader, reader1,writer1,i)


        #######


        # Calculate precision


        #######
        resultfilepath = '/Users/pengyuzhou/Downloads/Asvdplusplus.csv'
        csvfilepath = '/Users/pengyuzhou/Downloads/user-item-cf/train_output_cf_account_manager.csv'
