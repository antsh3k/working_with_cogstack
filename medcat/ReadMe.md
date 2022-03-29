# Medical <img src="../data/media/medcat_logo.png" width=45>oncept Annotation Tool

This directory contains information on retrieving data and creating models
All details regarding creating, building and running the NLP model are stored here.

## Locations for storing data:

- The [data](data) directory stores textual content. 
Methods for retrieving data should be stored in the [retrieve_data](search) folder.

- The [MedCAT models](data/medcat_models) directory holds models.

## Order of processing steps

#### __Step 1__: Create the model

Each of the model components are found [here.](medcat/1_create_model)
This directory contains all the components required to initialise a model pack.

All models should be stored [here.](data/medcat_models)


#### __Step 2__: Perform training

- __Step 2.1__: Unsupervised training

    The unsupervised training steps can be found within [train_model/unsupervised_training]()


 - __Step 2.2__: Supervised training

    After providing supervised labels with MedCATtrainer.
    The supervised training steps can be found within [train_model/supervised_training]()
 
#### __Step 3__: Run model

Run model on your corpus of documents and write to sql db.
Instructions on how to do this can be found within [run_model]()



