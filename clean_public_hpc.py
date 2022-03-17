from parameter_holder_hpc import *
__author__ = "Philipp Lang and Raphael Kronberg Department of Molecular Medicine II, Medical Faculty," \
             " Heinrich-Heine-University"
__license__ = "MIT"
__version__ = "1.0.1"
__status__ = "Prototype: This progam/code can not be used as diagnostic tool."
__credits__ = "Pls cite and refer to when using the code: Kronberg R. et al.," \
                "Communicator-driven Data Preprocessing Improves Deep Transfer Learning" \
                "of Histopathological Prediction of Pancreatic Ductal Adenocarcinoma.  , Journal, 2021"
if __name__ == '__main__':
    since = time.time()
    modelname = 'resnet'
    pixcut = 256
    #raw data test train val folder with data to clean up
    #cleanup_nets folder with nets class for class


    cls_net_dict_A = {'HP': 'train_model_resnet_Rev10_HP_BG_cleaning_256_resnet_A_02022_03_17__08_41_47.pth',
                      'HLN': 'train_model_resnet_Rev10_HLN_BG_cleaning_256_resnet_A_02022_03_16__11_03_04.pth',
                      'PDAC': 'train_model_resnet_Rev10_PDAC_BG_cleaning_256_resnet_A_02022_03_17__08_25_19.pth'}
    cls_net_dict_B = {'HP': 'train_model_resnet_Rev10_HP_BG_cleaning_256_resnet_B_02022_03_17__08_45_48.pth',
                      'HLN': 'train_model_resnet_Rev10_HLN_BG_cleaning_256_resnet_B_02022_03_16__11_33_52.pth',
                      'PDAC': 'train_model_resnet_Rev10_PDAC_BG_cleaning_256_resnet_B_02022_03_17__08_29_26.pth'}
    dict_of_alpha_cls = {'HP': ['ADI', 'BG','HP'],
                         'HLN': ['ADI', 'BG','HLN'],
                         'PDAC': ['ADI', 'BG','PDAC'],
                                                            }
    dict_of_alpha_cls_nl = {'HP': ['ADI', 'BG', 'HP', 'NL'],
                            'HLN': ['ADI', 'BG', 'HLN', 'NL'],
                            'PDAC': ['ADI', 'BG', 'PDAC', 'NL'],}
    print(cls_net_dict_A, cls_net_dict_B)
    print(dict_of_alpha_cls)
    for TVT in ['train', 'test', 'val']:
        for cls in ['HP','PDAC','HLN']:
            print(cls)
            print()
            arg_dict_A = create_arg_dict(reload=True, batch_size=1, data_load_shuffle=False,
                                       session_id = 'resnet_Rev10_cleanUp_{}_{}_TileNorm_run_01'.format(cls, modelname),
                                       normalize_on=0, label_coloring=False,
                                       Not_TTC='None', treshhold=0.55,
                                       folder_path='./data/CD_Spots_test/{}/{}'.format(TVT,cls),#'./data/Com_Data/{}/{}'#only patch foilder not images/Spots
                                       reload_path='./saved_models/{}'.format(cls_net_dict_A[cls]),
                                       train_tile_classes = dict_of_alpha_cls[cls],
                                       class_names = dict_of_alpha_cls_nl[cls], pixel_cutoff= pixcut,#239
                                       save_class_patches = True,
                                       save_class_patches_path ='./patches_A_{}/'.format(modelname),
                                       save_class_patches_mod = TVT,
                                       save_class_patches_class = cls,
                                       patches_mod=True,
                                       model_name=modelname,
                                       )#add not_ttc
            args_A = get_arguments(arg_dict_A)
            TA = Trainer(args_A)
            TA.inference_folder_new()
            ###
            arg_dict_B = create_arg_dict(reload=True, batch_size=1, data_load_shuffle=False,
                                         session_id='resnet_Rev10_cleanUp_{}_{}_TileNorm_run_02'.format(cls, modelname),
                                         normalize_on=0,
                                         label_coloring=False,
                                         Not_TTC='None', treshhold=0.55,
                                         folder_path='./patches_A_{}/{}/{}'.format(modelname, TVT, cls),
                                         reload_path='./saved_models/{}'.format(cls_net_dict_B[cls]),
                                         train_tile_classes=dict_of_alpha_cls[cls],
                                         class_names=dict_of_alpha_cls_nl[cls], pixel_cutoff=pixcut,#239
                                         save_class_patches=True,
                                         save_class_patches_path='./patches_B_{}/'.format(modelname),
                                         save_class_patches_mod=TVT,
                                         save_class_patches_class=cls,
                                         patches_mod=True,
                                         model_name=modelname,
                                         )  # add not_ttc
            args_B = get_arguments(arg_dict_B)
            TB = Trainer(args_B)
            TB.inference_folder_new()
            print('end of {}'.format(cls))

    time_elapsed = time.time() - since
    print('Clean up complete in {:.0f}m {:.0f}s'.format(time_elapsed // 60, time_elapsed % 60))
