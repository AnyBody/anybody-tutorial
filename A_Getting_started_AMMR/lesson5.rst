The Typical (and Recommended) Structure of Application Models
=============================================================

There is no unique way to setup an application model. A model might look
different for each user and each case. Models will also be different
depending on the skills of the user. Here are some examples how a model
can be structured. Good examples are the StandingMan, the MoCap Model,
and the BikeModel, but even those differ slightly due to their different
creators:

Typically, you can find 3 folders and one (or several) main files in the
application. The *main file* (\*.main.any) is the file to load in
AnyBody and from where you run the application. There is an Input folder
that contains the data necessary as input for the application, this can
be for example motion capture (C3D) files for a MOCAP driven model, or
it can be the geometry files (STL) of a bike. The Output folder is empty
by default, but many models have a switch (a #define statement) to save
the model as H5 anydata files into the output folder. These files
contain basically every output data and can be loaded again at a later
time point to look at graphs again or to replay the motion again. In the
Model folder, you can find all the AnyScript files that implement the
application model. We do not recommend to edit those files separately.
The best is to load the main file and look at the structure of the
model. By opening the included file from the model (either by
double-clicking on the #include-statement in an already opened file or
by selection in the File Tree), you can make alterations to the files
from there. You can see immediately by reloading (press F7) if the
changes will cause the desired outcome or a failure to correct before
continuing.

Here comes a number of typical item of the application models that are
worth to notice:

1. **Library definition (libdef.any):** Usually, a main file starts with
   the inclusion of the libdef.any, a file that creates the link to the
   body folder as well as other so-called library settings. A model
   library is basically a folder with a libdef.any file in; here you
   specify parameters to be shared by the whole library of models). In
   practice, you can, therefore, have an application model in a
   different location than the AMMR Application folder, meaning that the
   application could be in "MyFiles" on your computer, while the body
   model is the installed version next to the AnyBody software in
   "Program Files". This requires only the right path definition in this
   libdef.any file for your library in "MyFiles". (Occationally, a
   libdef.any only points to "../libdef.any" etc. and only the top one
   contains the actual library definitions incl. the path of the body
   model).

2. **Model Description:** Most models have either a separate file called
   description in the top, or a detailed description in code, of the
   functionality and features of the application. Please read that
   description carefully to see if the model suits you. And as a model
   author, it is of course recommended to maintain it well for own and
   others purpose. Please notice, the functionality of making so-called
   Documentation Comments in the code; Documentation Comments are
   in-code comments that will be attached to the associated object in
   the model and will be displayed when navigating the model for
   instance in the Model Tree. This makes your effort in mode
   documentation far more transparent to other users. (Notice that
   Documentation Comments are typically made with /// instead of normal
   // for code comments; see the AnyScript Reference Manual for more
   details)

3. **Standard Output:** Typical main files have a switch to export the
   results as mentioned above or not. By default this is set to 0,
   meaning it is off, you can change it to 1 to save the output after
   each simulation. Please be aware that in most cases the existing H5
   output file will be overwritten after running a new simulation.
   Additionally, you should be aware, that those H5 files contain a lot
   of data and can be very large for complex models. Finally, notice
   that it is recommended to use the standard output path definition
   (typically provided in the Library definitions in libdef.any). This
   ensures that the output of all models in the library
   easily/systematically can be directed to an external location outside
   the folders of your model. This can be very beneficial when
   processing large data sets and using many different model parameters
   (or even model version).

4. **Run Application operation:** Many main files (typically in the
   Demos of the AMMR) have a RunApplication file included that
   implements the RunApplication operation which is found on the left
   side of the AMS in the Operations tab. It contains the sequence
   operations of what studies to be executed. This is the model author's
   way of showing which operations that are expected to execute and to
   make it easy for you to do so. This concept can also be recommended
   for your own models.

5. **Main items in the Model Tree:** Most basic models have three basic
   levels, a Main level, a Main.Model level, and a Main.Study level. It
   is recommended to keep this structure for new or altered models. In
   most models, the human model is included in the Main level. The
   Main.Model level includes this human model using a reference and adds
   an environment to it. The Main.Study level includes the Main.Model
   using a reference. This structure allows having several studies using
   the same model (i.e. Main.Model), but applying different analyses to
   it. This structure is also prepared for having multiple models, i.e.,
   Main.Model1 and Main.Model2 that may use the same HumanModel but in
   different context.