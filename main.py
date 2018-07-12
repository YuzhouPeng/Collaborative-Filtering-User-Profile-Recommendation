import matrix_generator, globalparameter, csv

if __name__ == '__main__':
    reader = csv.reader(open(globalparameter.folderpath[0] + '/' + 'output_pos_for_dummy.csv', 'r'))
    reader1 = csv.reader(open(globalparameter.folderpath[0] + '/' + 'output_neg_for_dummy.csv', 'r'))
    writer = csv.writer(open(
        globalparameter.collaborative_filtering_path + '/test_output_cf_' + globalparameter.jobtitle_list[0] + '.csv',
        'w'))
    writer1 = csv.writer(open(
        globalparameter.collaborative_filtering_path + '/train_output_cf_' + globalparameter.jobtitle_list[0] + '.csv',
        'w'))
    matrix_generator.matrix_generator_train(
        globalparameter.folderpath[0] + '/' + 'output_pos_for_dummy.csv',
        globalparameter.folderpath[0] + '/' + 'output_neg_for_dummy.csv', globalparameter.jobtitle_list[0],
        globalparameter.jobtitle_path_list[0], 0.5, reader, reader1,writer1)
    matrix_generator.matrix_generator_test(globalparameter.folderpath[0] + '/' + 'output_pos_for_dummy.csv',
                                           globalparameter.folderpath[0] + '/' + 'output_neg_for_dummy.csv',
                                           globalparameter.jobtitle_list[0],
                                           globalparameter.jobtitle_path_list[0], 0.5,reader,reader1,writer)
