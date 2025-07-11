.. SpaCon_tutorials documentation master file, created by
   sphinx-quickstart on Wed Jul  9 14:36:26 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


This is SpaCon’s documentation
========================================

**SpaCon**: Integrative Analysis of **Spa**tial Transcriptome and **Con**nectome

========================================



.. toctree::
   :maxdepth: 2
   :caption: Contents:

   SpaCon_tutorial1_for_mouse_3D_ST
   SpaCon_tutorial2_for_mouse_celltype_classification
   SpaCon_tutorial3_for_mouse_widefield_FC_data
   SpaCon_tutorial4_for_marmoset_ST_and_FC


.. image:: ./Workflow.png
   :width: 1600 




Overview
========
The brain’s structure and function arise from its complex molecular composition and neural connectivity, yet the relationship between cell-type-specific gene expression and brain-wide connectivity is not well understood. By integrating single-cell resolution spatial transcriptomics and connectomics, we reveal a tight coupling between gene expression and anatomical connectivity in the cortico-thalamic circuit, and identify specific gene expression in axons of the corpus callosum that reflect their cortical origins. Building on these findings, we developed SpaCon, a graph attention autoencoder that uses a tunable hyperparameter to flexibly integrate global connectivity with local gene expression. To enable analysis at the whole-brain scale, SpaCon introduces an efficient neighbor sampling strategy that drastically reduces computational requirements without compromising performance. This architecture allows the model to identify functionally relevant three-dimensional domains defined by both molecular identity and shared connectivity patterns, even when spatially distant. Validated across diverse datasets and species, SpaCon significantly enhances the prediction of connectivity from gene expression and improves the spatial classification of neuronal subtypes. SpaCon thus provides a powerful, scalable, and versatile framework for understanding the complex relationship between transcriptome and connectome.
