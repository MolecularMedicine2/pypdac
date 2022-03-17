from parameter_holder_hpc import*
import os
import time
import numpy as np

__author__ = "Philipp Lang and Raphael Kronberg Department of Molecular Medicine II, Medical Faculty," \
             " Heinrich-Heine-University"
__license__ = "MIT"
__version__ = "1.0.1"
__status__ = "Prototype: This progam/code can not be used as diagnostic tool."
__credits__ = "Pls cite and refer to when using the code: Kronberg R. et al.," \
                "Communicator-driven Data Preprocessing Improves Deep Transfer Learning" \
                "of Histopathological Prediction of Pancreatic Ductal Adenocarcinoma.  , Journal, 2021"


def datestr():
    ''' get the date for naming of files '''
    temp_time = '{:04}_{:02}_{:02}__{:02}_{:02}_{:02}'.format(time.gmtime().tm_year, time.gmtime().tm_mon,
                                                              time.gmtime().tm_mday, time.gmtime().tm_hour,
                                                              time.gmtime().tm_min, time.gmtime().tm_sec)
    return temp_time


def train_block(file_path_train, add_img_path, cname, count, modelname, pixelcut, Clean_up_class):
    print('type',train_tile_classes )
    arg_dict_A = create_arg_dict(reload=False, add_img=True, file_path_train=file_path_train,
                                 add_img_path=add_img_path, Not_TTC=Clean_up_class,
                                 session_id ='train'.format(cname, count),
                                 train_val_test=train_val_test,
                                 train_tile_classes=train_tile_classes,
                                 class_names=class_names,
                                 pixel_cutoff=pixelcut,
                                 model_name=modelname,
                                 result_file_name='Rev10_{}_BG_cleaning_{}_{}_{}_{}'.format(Clean_up_class, pixelcut, modelname,
                                                                                   cname, count),
                                 model_id='Rev10_{}_BG_cleaning_{}_{}_{}_{}'.format(Clean_up_class, pixelcut, modelname, cname,
                                                                           count),
                                 )
    args_A = get_arguments(arg_dict_A)
    T_A = Trainer(args_A)
    model_path = T_A.model_train()[0]
    return model_path

def inference_block(pre_path, path_in, Clean_up_class, model_path, cname, count, modelname,pixelcut):
    for tvt in train_val_test:
        path_1 = os.path.join(path_in, tvt, Clean_up_class)
        s_path = pre_path + '{}'.format(tvt) +'/{}/'.format(Clean_up_class)
        temp_p= pre_path + '{}'.format(tvt)
        os.mkdir(temp_p)
        os.mkdir(s_path)
        arg_dict = create_arg_dict(folder_path=path_1, reload=True, batch_size=1, data_load_shuffle=False,
                                   session_id='inference_{}_{}'.format(cname, count), normalize_on=0, label_coloring=False,
                                   save_class_dir=s_path,
                                   Not_TTC=Clean_up_class, train_val_test=train_val_test,
                                   train_tile_classes=train_tile_classes, class_names=class_names,
                                   reload_path= model_path,
                                   save_colored_dir=bin_path,
                                   pixel_cutoff=pixelcut,
                                   model_name=modelname,
                                   result_file_name='Rev10_{}_BG_cleaning_{}_{}_{}_{}'.format(Clean_up_class, pixelcut, modelname, cname, count),
                                   model_id='Rev10_{}_BG_cleaning_{}_{}_{}_{}'.format(Clean_up_class, pixelcut, modelname, cname, count),  # 'my_model_pathoFIT_18_final',
                                   )
        args = get_arguments(arg_dict)
        T1 = Trainer(args)
        T1.inference_folder_new()
    return pre_path

if __name__ == '__main__':
    time.sleep(5)
    modelname = 'resnet'
    pixelcut  = 256
    bin_path = './data/bin_{}_{}/'.format(datestr(), np.random.randint(1))
    os.mkdir(bin_path)
    Clean_up_class = 'HP'
    train_val_test = ['train', 'val', 'test']
    train_tile_classes = ['ADI', 'BG', Clean_up_class]
    class_names = ['ADI', 'BG', Clean_up_class, 'NL']
    number_of_iterations = 1
    dataset_list = []
    path_in = '.\data\CD_K_Data' #'./data/CD_K_Data/'
    path_spots_a = '.\data\CD_D_spots_{}1'.format(Clean_up_class)#'./data/CD_D_spots_HLN1/'
    path_spots_b = '.\data\CD_D_spots_{}2'.format(Clean_up_class) #'./data/CD_D_spots_HLN2/'
    list_A = []
    list_B = []
    model_path_list_A = []
    model_path_list_B = []
    for i in range(number_of_iterations):
        pre_path_A = './results/clean_up_{}_{}_{}_counter_{}_{}/'.format(Clean_up_class, datestr(), 'A',i, modelname)
        pre_path_B = './results/clean_up_{}_{}_{}_counter_{}_{}/'.format(Clean_up_class, datestr(), 'B',i, modelname)
        os.mkdir(pre_path_A)
        os.mkdir(pre_path_B)
        list_A.append(pre_path_A)
        list_B.append(pre_path_B)
        if i ==0:
            add_img_path_A = path_spots_b
            add_img_path_B = path_spots_a
        #train net A and net B
        print('step {} train net A'.format(i))
        temp_net_A_path = train_block(path_in,add_img_path_B,cname='A', count=i, modelname= modelname, pixelcut = pixelcut, Clean_up_class = Clean_up_class)
        model_path_list_A.append(temp_net_A_path)
        print('model A path: {}'.format(temp_net_A_path))
        print('step {} finish training net A'.format(i))

        print('step {} train net B'.format(i))
        temp_net_B_path = train_block(path_in,add_img_path_A,cname='B', count=i, modelname= modelname, pixelcut = pixelcut, Clean_up_class = Clean_up_class)
        model_path_list_B.append(temp_net_B_path)
        print('model B path: {}'.format(temp_net_B_path))
        print('step {} finish training net B'.format(i))

        # infer with net A and B the spots A and B
        add_img_path_B = inference_block(pre_path=pre_path_B, path_in=path_spots_a, Clean_up_class=Clean_up_class, model_path=temp_net_B_path,cname='B', count=i, modelname= modelname, pixelcut = pixelcut)
        add_img_path_A = inference_block(pre_path=pre_path_A, path_in=path_spots_b, Clean_up_class=Clean_up_class, model_path=temp_net_A_path,cname='A', count=i, modelname= modelname, pixelcut = pixelcut)
    print(list_A)
    print(list_B)
    print(model_path_list_A)
    print(model_path_list_B)









