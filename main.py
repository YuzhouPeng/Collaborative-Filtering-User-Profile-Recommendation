import matrix_generator, globalparameter, csv

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
        # reader = csv.reader(open(globalparameter.folderpath[i] + '/' + 'output_pos_for_dummy.csv', 'r'))
        # reader1 = csv.reader(open(globalparameter.folderpath[i] + '/' + 'output_neg_for_dummy.csv', 'r'))
        # matrix_generator.matrix_generator_test(globalparameter.folderpath[i] + '/' + 'output_pos_for_dummy.csv',
        #                                        globalparameter.folderpath[i] + '/' + 'output_neg_for_dummy.csv',
        #                                        globalparameter.jobtitle_list[i],
        #                                        globalparameter.jobtitle_path_list[i], 0.5,reader,reader1,writer,i)
