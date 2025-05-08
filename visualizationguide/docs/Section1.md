# Introduction

<style>
    .link {
        text-align: center;
        font-size: 16px;
    }
    .textstuff {
        font-size: 17px;
    }
</style>

VisIt is an open-source visualization and analysis tool for large data sets often used to create
computationally complex visualizations. The uniqueness of VisIt that separates it from similar
visualization software lies in the method in which it handles and models the input data. Rendering
realistic physics simulations is often computationally intensive, especially when using the massive
data sets output by large-scale numerical simulations. Optimized processing and rendering techniques
are crucial in the field of numerical relativity for this very reason, as creating accurate and self-
consistent visualizations is impossible without these added techniques due to the magnitude of
complexity involved in the data itself.

The first part of this guide is geared as a general overview of VisIt for numerical relativity
researchers. We will go over the installation process and user guide for local machines and
supercomputers. Then we will introduce relevant aspects of VisIt by walking through sample
visualizations using small datasets. After this introduction, we will discuss a typical workflow with
VisIt in numerical relativity before providing a suite of case studies of visualizations we’ve made
over the past years and the specific techniques we used.

Throughout the document, we will reference small data files and scripts, which can be found in
the following repository:

<div class="link">
<a href="https://github.com/tsokaros/Illinois-NR-VisIt-Guide"><code>https://github.com/tsokaros/Illinois-NR-VisIt-Guide</code></a>
</div>
<br>



We will reference this repository using the prefix <code style="font-size: 13px;">VisIt-Guide</code>. If we want to point to a file called <code style="font-size: 13px;">ex_file.ext</code> located in the folder <code style="font-size: 13px;">ex_folder</code> inside of the repository, we will write 
<a href="https://github.com/tsokaros/Illinois-NR-VisIt-Guide/blob/main/ex_folder/ex_file.ext"><code style="font-size: 13px;">VisIt-Guide/ex_folder/ex_file.ext</code></a>. These file locations will also be hyperlinks that point to the file on GitHub.
