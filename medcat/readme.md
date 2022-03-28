# MedCAT

This directory contains information on retrieving data and creating models
All details regarding creating, building and running the NLP model are stored here.

## Locations for storing data:

- The [data](data) directory stores MedSHR textual content. 
Methods for retrieving data should be stored in the [retrieve_data](search) folder.

- The [models](data/models) directory holds models.

## Order of processing steps

__Step 1__: Create the model

Each of the model components are found [here.](medcat/create_model)
This directory contains all the components required to initialise a model pack.

All models are stored [here.](data/models)


__Step 2__: Perform unsupervised training

The unsupervised training steps can be found within [train_model/unsupervised_training]()


__Step 3__: Supervised training

After providing supervised labels with MedCATtrainer.
The supervised training steps can be found within [train_model/supervised_training]()
 
__Step 4__: Run model

Run model on your corpus of documents and write to sql db.
Instructions on how to do this can be found within [run_model]()



