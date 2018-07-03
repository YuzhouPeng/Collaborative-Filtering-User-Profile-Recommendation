import matrix_generator, globalparameter

if __name__ == '__main__':
    matrix_generator.matrix_generator_train(
        globalparameter.folderpath[0] + '/' + 'output_pos_for_dummy.csv',
        globalparameter.folderpath[0] + '/' + 'output_neg_for_dummy.csv', globalparameter.jobtitle_list[0],
        globalparameter.jobtitle_path_list[0], 0.5)
    matrix_generator.matrix_generator_test(globalparameter.folderpath[0] + '/' + 'output_pos_for_dummy.csv',
                                           globalparameter.folderpath[0] + '/' + 'output_neg_for_dummy.csv',
                                           globalparameter.jobtitle_list[0],
                                           globalparameter.jobtitle_path_list[0], 0.5)
