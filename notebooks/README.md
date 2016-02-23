# README #

The links below are to static renderings of the notebooks via nbviewer.ipython.org. Descriptions below the links are from the first cell of the notebooks (if that cell contains Markdown or raw text).

##Test mytrc function

* ##[ [ORCA_offline]TestMytrc.ipynb](http://nbviewer.jupyter.org/urls/bitbucket.org/ccar-modeling/analysis/raw/fd8ee7611eb3e0e6d6f2281a31c88ba97ab1e1c0/Cindy Yu/[ORCA_offline]TestMytrc.ipynb)

##Initial field for 231Pa, 230Th and their ratio

* ##[[initial_condition]ANHA_part_Pa.ipynb](http://nbviewer.jupyter.org/urls/bitbucket.org/ccar-modeling/analysis/raw/b0f492b9ad588358305425ed798ab21ea926b733/Cindy Yu/ANHA_initial/[initial_condition]ANHA_part_Pa.ipynb)

* ##[[initial_condition]ANHA_diss_Pa.ipynb](http://nbviewer.jupyter.org/urls/bitbucket.org/ccar-modeling/analysis/raw/b0f492b9ad588358305425ed798ab21ea926b733/Cindy Yu/ANHA_initial/[initial_condition]ANHA_diss_Pa.ipynb)

* ##[[initial_condition]ANHA_part_Th.ipynb](http://nbviewer.jupyter.org/urls/bitbucket.org/ccar-modeling/analysis/raw/0bb31ff77d094907c0901d01481fd98f10b0f8f9/Cindy Yu/ANHA_initial/[initial_condition]ANHA_part_Pa.ipynb)

* ##[[initial_condition]ANHA_diss_Th.ipynb](http://nbviewer.jupyter.org/urls/bitbucket.org/ccar-modeling/analysis/raw/0bb31ff77d094907c0901d01481fd98f10b0f8f9/Cindy Yu/ANHA_initial/[initial_condition]ANHA_diss_Th.ipynb)

* ##[[initial_condition]ratio.ipynb](http://nbviewer.jupyter.org/urls/bitbucket.org/ccar-modeling/analysis/raw/b0f492b9ad588358305425ed798ab21ea926b733/Cindy Yu/ANHA_initial/initialPaTh_field.ipynb)


##Change mask_mesh in Canada Basin

* ##[[mesh_mask]First_change.ipynb](http://nbviewer.jupyter.org/urls/bitbucket.org/ccar-modeling/analysis/raw/tip/Cindy%20Yu/ANHA4-result/Anormal_at_bottom/1_change_mask_mesh%28magic!%29.ipynb?at=default&fileviewer=file-view-default)

##Add two more tracers in the model to simulate the imaginary particles
* ##[[six_tracers_tracer_plots.ipynb]](http://nbviewer.jupyter.org/urls/bitbucket.org/ccar-modeling/analysis/raw/a6b543f800f1a62a713193ef0f59ebb264e89874/Cindy Yu/ANHA4-result/Anormal_at_bottom/six_tracers_tracer_plots.ipynb)

* ##[[six_tracers_TS_plots.ipynb]](http://nbviewer.jupyter.org/urls/bitbucket.org/ccar-modeling/analysis/raw/a6b543f800f1a62a713193ef0f59ebb264e89874/Cindy Yu/ANHA4-result/Anormal_at_bottom/six_tracers_TS_plots.ipynb)
This notebook displays u,v,w,s,t from Xianmin's output.

##Add bbc at the bottom

* ##[[Addbbc_Testbbc.ipynb]](http://nbviewer.jupyter.org/urls/bitbucket.org/ccar-modeling/analysis/raw/tip/Cindy%20Yu/ANHA4-result/Add_bbc_for_tracers/Addbbc_Testbbc.ipynb) 
The value in bottom layer is not reasonable. Therefore, a bbc is added at the deepest grid. This notebook is used to test the bbc.

* ##[[Addbbc_Result_20020101_6h.ipynb]](http://nbviewer.jupyter.org/urls/bitbucket.org/ccar-modeling/analysis/raw/tip/Cindy%20Yu/ANHA4-result/Add_bbc_for_tracers/Addbbc_Result_20020101_6h.ipynb) 
The offline model was run for 1 day with bbc added into trcnxt.F90. This notebook displays the model output.

* ##[[Investigate_bottom_layers.ipynb]](http://nbviewer.jupyter.org/urls/bitbucket.org/ccar-modeling/analysis/raw/tip/Cindy%20Yu/ANHA4-result/Add_bbc_for_tracers/Investigate_bottom_layers.ipynb)
 Plot tracer field, imaginary ice, sinking rate, absorption rates from my model along with u,v,w,eddy coeff,s,t from Xianmin's output.

* ##[[check_mesh_mask.ipynb]](http://nbviewer.jupyter.org/url/bitbucket.org/ccar-modeling/analysis/raw/tip/Cindy%20Yu/ANHA4-result/Add_bbc_for_tracers/check_mesh_mask.ipynb) 
This notebook aims at taking a look at the grids at bottom layers in order to fix this problem.


##Add tmask in trcsms_my_trc.F90

* ##[[Top+Horiz_view.ipynb]](http://nbviewer.jupyter.org/urls/bitbucket.org/ccar-modeling/analysis/raw/tip/Cindy%20Yu/ANHA4-result/Add_tmask_in_trcsms/Top+Horiz_view.ipynb) 
This notebook displays model output from the run with tmask added in trcsms_my_trc.F90.


* ##[[mesh_mask_plot.ipynb]](http://nbviewer.jupyter.org/urls/bitbucket.org/ccar-modeling/analysis/raw/tip/Cindy%20Yu/ANHA4-result/Add_tmask_in_trcsms/mesh_mask_plot.ipynb) 
This notebook displays vertical tracer profiles with w and t grid lines.

* ##[[C-grid.ipynb]](http://nbviewer.jupyter.org/urls/bitbucket.org/ccar-modeling/analysis/raw/tip/Cindy%20Yu/ANHA4-result/Add_tmask_in_trcsms/C-grid.ipynb)
This notebook explores the structure of c-grid. 


## Change bahty. (fse3t)

* ##[[mesh_mask.ipynb]](http://nbviewer.jupyter.org/urls/bitbucket.org/ccar-modeling/analysis/raw/tip/Cindy%20Yu/ANHA4-result/Change_bahty_fse3t_based/mesh_mask_fse3t.ipynb)

* ##[[Horizontal+Time-quick-test.ipynb]](http://nbviewer.jupyter.org/urls/bitbucket.org/ccar-modeling/analysis/raw/tip/Cindy%20Yu/ANHA4-result/Change_bahty_fse3t_based/Horizontal+Time-quick-test.ipynb)


* ##[[Horizontal+Time-from2002to5.ipynb]](http://nbviewer.jupyter.org/urls/bitbucket.org/ccar-modeling/analysis/raw/tip/Cindy%20Yu/ANHA4-result/Change_bahty_fse3t_based/Horizontal+Time-from2002to5.ipynb)
