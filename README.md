## DeepLearning_Abeta [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/gamazonlab/DeepLearning_Abeta/blob/master/LICENSE)

Alzheimer’s Disease (AD) is a debilitating form of dementia with a high prevalence in the global population and a large burden on the community and health care systems. AD’s complex pathobiology consists of extracellular β-amyloid deposition and intracellular hyperphosphorylated tau. Comprehensive mutational analyses can generate a wealth of knowledge about protein properties and enable crucial insights into molecular mechanisms of disease. Deep Mutational Scanning (DMS) has enabled multiplexed measurement of mutational effects on protein properties, including kinematics and self-organization, with unprecedented resolution. However, potential bottlenecks of DMS characterization include experimental design, data quality, and the depth of mutational coverage. Here, we apply Deep Learning to comprehensively model the mutational effect of the AD-associated peptide Aβ42 on aggregation-related biochemical traits from DMS measurements. Among tested neural network architectures, Convolutional Neural Networks (ConvNets) and Recurrent Neural Networks (RNN) are found to be the most cost-effective models with robust high performance even under insufficiently-sampled DMS studies. While sequence features are essential for satisfactory prediction from neural networks, geometric-structural features further enhance the prediction performance. Notably, we demonstrate how mechanistic insights into phenotype may be extracted from the neural networks themselves suitably designed. This methodological benefit is particularly relevant for biochemical systems displaying a strong coupling between structure and phenotype, as shown here for the relationship between the conformation of Aβ42 aggregate and nucleation, using a Graph Convolutional Neural Network (GCN), with the network architecture developed from the protein atomic structure input. Importantly, the mutationally-defined nucleation phenotype generated from a neural network shows improved resolution for identifying known disease-causing mutations relative to the original DMS phenotype. Our study suggests that neural network derived sequence-phenotype mapping can be exploited not only to provide direct support for protein engineering but also to facilitate therapeutic design with the gained perspectives from biological modeling.

### Reference
Towards mechanistic models of mutational effects: Deep Learning on Alzheimer’s Aβ peptide  
Bo Wang*, Shahab Razavi*, Eric R. Gamazon  
*Equal contribution  
Contact:  ericgamazon@gmail.com

#### Acknowledgement
This repository builds on the nn4dms pipeline from the Gitter Lab.  
Neural networks to learn protein sequence-function relationships from deep mutational scanning data. Sam Gelman, Sarah A Fahlberg, Pete Heinzelman, Philip A Romero+, Anthony Gitter+. Proceedings of the National Academy of Sciences, 118:48, 2021.
