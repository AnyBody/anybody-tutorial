Lesson 7: Wrapping the Model with AnyBody Project
=================================================

“AnyBody Project” or just AnyProject, since it is defined with this
class name, is a data structure aimed at wrapping a model and bringing
its important features to the surface in AnyBody GUI and thereby closer
to the user.

The objective is to ease execution of important model’s operations and
related actions and collect these in a dedicated and intuitive place.
This is equally aimed at the experienced and advanced user doing
repetitive work with many models or many data sets, users working with
models prepared by others, and the less experienced users who need to
work with a model for processing data, but who does not have to develop
it or understand it’s every detail.

The AnyProject functions can be summarized by

-  Model View Definitions that provide features for defining particular
   views of the model and user interface for activating the views.

-  Task definitions that wrap the important operations of the model with
   a user interface for execution. A Model View Definition can be
   associated with a given task.

-  All project objects are equipped with descriptions that can be used
   for explaining the task or view to new users.

-  Project file information is automatically found by the system and can
   be supplemented by the user.

-  “Send to” function for exporting the model and all of its resources
   to a new location

An AnyBody project is defined in the model, in principle as any other
objects of the model using the AnyProject class. The main difference to
most objects is that project objects do not provide new information by
themselves, but merely collect information to the AnyBody Modeling
System GUI about what is important in the particular model.

In this lesson, we shall make an AnyBody Project wrapper of the very
simple planar arm model (:download:`Demo.arm2d.any <Downloads/demo.arm2d.any>`
using :download:`dumbbell.stl <Downloads/dumbbell.stl>`) that we have used in
previous lessons. The final example file we shall build in this lesson
is :download:`AnyProject.any <Downloads/AnyProject.any>` using
:download:`DrawGroups.any <Downloads/DrawGroups.any>` in addition.

We include the model file in our new main file, and we create an empty
project called ArmProject.

.. code-block:: AnyScriptDoc

    
    Main = {
    
        #include "Demo.arm2d.any"
    
        AnyProject ArmProject = {
    
        };
    
    }; // Main
    


Project Files
-------------

Firstly, we add some file information to the project. This is done in
the AnyProject Files folder, which is a predefined folder. Here we set
two files, the MainFile and the SetValueFile.

.. code-block:: AnyScriptDoc

    
    Main = {
    
        #include "Demo.arm2d.any"
    
         AnyProject ArmProject = {
    
            Files = {
    
                MainFile = "AnyProject.any";
    
                SetValueFile = "values.anyset";
    
            };
    
        };
    
    }; // Main
    


The MainFile indicates simply which file is the main file for this
project. It may seem a bit redundant, but this information also serves
to determine whether the project is active or not. Multiple projects can
in principle exist in the model, but only the one(s) having the correct
main file is considered active by the system.

This implies that we can include a file that is actually a Main file by
itself (as in this case with Demo.arm2d.any), and this main file could,
in fact, have a project (AnyProject) of its own, but it would only be
active if we actually load the arm2d.any. In the given example we have
only one AnyProject.

The SetValueFile is a file used by the project for storing modified
values. It is automatically saved when closing the model and
automatically loaded, although only upon user acceptance when loading
the model. Apart from this, it is saved and loaded exactly like the
manual execution of the Main folder’s Class Operations, “Save Values”
and “Load Values”, respectively.

The SetValueFile needs not to be specified, and it will only be managed
by active projects, i.e. projects with a MainFile specification matching
the loaded Main file.

The Files folder also contains some file-objects for storing project
file information. These are automatically filled during loading. Their
information can, of course, be accessed or just inspected by the user,
but it is also used during “Send to” export operations on the model
(Class Operation of Main). It should, however, be noticed that the “Send
to” Class Operation to some extent is functional for models without
project information too.

Model View Definitions
----------------------

Model View Definitions are basically a set of view actions applied to a
number of drawing groups. In order to set up some standard views for the
model, we shall, therefore, define some drawing groups:

.. code-block:: AnyScriptDoc

    Main = {
    
    ...
    
    AnyFolder DrawGroups = {
        
        AnyDrawGroup AllSegments = {
        
        Objects = ObjSearch("Main.ArmModel.Segs.*");
        
        };
        
        AnyDrawGroup AllMuscles = {
        
        Objects = ObjSearch("Main.ArmModel.Muscles.*");
        
        };
        
        AnyDrawGroup AllDeltoidMuscles = {
        
        Objects = ObjSearch("Main.ArmModel.Muscles.Del*.DrwMus");
        
        };
        
        AnyDrawGroup All = {
        
        Objects = ObjSearchRecursive("Main.ArmModel","*");
        
        };
        
    };
    
    ...
    
    }; // Main

    


In the final example files, this is actually done in a separate file,
:download:`DrawGroups.any <Downloads/DrawGroups.any>`, so we now have

.. code-block:: AnyScriptDoc

    Main = {
    
    #include "Demo.arm2d.any"
    
    #include "DrawGroups.any"
    
    AnyProject ArmProject = {
        
        Files = {
        
        MainFile = "AnyProject.any";
        
        SetValueFile = "values.anyset";
        
        };
        
    };
    
    }; // Main


    


Having defined the draw groups we need, we can return to the project
definition and define our view

.. code-block:: AnyScriptDoc

    Main = {
    
    #include "Demo.arm2d.any"
    
    #include "DrawGroups.any"
    
    AnyProject ArmProject = {
        
        Views = {
        
            AnyProjectModelViewDefinition View_Misc = {
                
                DrawGroupSequence = {
                    &Main.DrawGroups.AllSegments,
                    &Main.DrawGroups.AllMuscles,
                    &Main.DrawGroups.AllDeltoidMuscles
                };
                
                Reset = {Off, Off, Off}; //Same behavior as not defining Reset.
                Hide = {Off, Off, Off}; //Same behavior as not defining Hide.
                ShowModelDefined = {On, Off, On};
                ShowAutoGenerated = {Off, On, Off}; //Same behavior as {Off, On}.
                Transparent = {On, Off, On};
                Select = {Off, Off, Off}; //Same behavior as not defining Select.
                
            };
        
        };
    
    ...
    


This view we define using three draw groups, all segments, all muscles
and the deltoid muscles. We want to show the model-defined segments and
deltoid muscle being transparent and the rest of the muscles will just
show their default drawing.

In the final example model you can download, we have defined three other
views, just to show how it works. For further information on how to
define Model View Definitions, please refer to the Reference Manual.

Project Tasks
-------------

Firstly, we define two simple tasks that execute the two important
operations of our main (our only) study. It executes the setting of
initial positions and inverse dynamics. These tasks are created by
defining two AnyProjectTaskOperation objects that point to the
particular operations in ArmModelStudy.

.. code-block:: AnyScriptDoc
 
    Main = {
    
    #include "Demo.arm2d.any"
    
    #include "DrawGroups.any"
    
    AnyProject ArmProject = {
        
        Tasks = {
        
        AnyProjectTaskOperation Set_Initial_Conditions = {
            
            Description = {
                Title = "Initial Conditions of Arm Model";
                BodyText = "This task sets the initial conditions.";
                Tooltip = "Sets Initial Conditions";
                Files = {"dumbbell.stl","values.anyset"};
            };
            
            Operation = &Main.ArmModelStudy.InitialConditions;
            
        };
        
        AnyProjectTaskOperation Run_Inverse_Dynamics = {
            
            Description = {
                Title = "Inverse Dynamcis of Arm Model";
                BodyText = "This task executes the inverse dynamics analysis of the arm model.";
                Tooltip = "Inverse Dynamics Simulation";
            };
            
            Operation = &Main.ArmModelStudy.InverseDynamics;
        };
    };
    ...
    

Each task is accompanied by a description consisting of a title, a body
text, and a tooltip string. All strings will appear in the AnyBody GUI
in the Projects pane. Additionally, the description can hold a list of
files. Here we have just added links to some file that are already part
of the model, but a more relevant case could be to make links to
external documentation related to the given task and model.

In addition to these options for executing the model, we want to equip
the model with tasks for saving and loading the simulated output. This
can be done by declaring an AnyOperationMacro object that calls the
Class Operations for “Save data” and “Load data” on the output folder
for MainArmModel.Study. All this, we do inside the task folder
definition because it is not part of the original model, see the
following code:

.. code-block:: AnyScriptDoc

    Main = {
    
    #include "Demo.arm2d.any"
    
    #include "DrawGroups.any"
    
    AnyProject ArmProject = {
        
        Tasks = {
        
        ...
        
        AnyProjectTaskOperation Save_Output_Data = {
            
            Description = {
            Title = "Saving output data from the simulation";
            BodyText = "This task saves the output for the simulation, e.g. executed by task " 
                        + strquote( AnyBodyLinkOf(&..Run_Inverse_Dynamics) )
                        + " to file "      
                        + strquote( strlink(.filename) );
            Tooltip = "Saving output data";
            Files = .filename;
            };
            
            Operation = &Opr;
            
            AnyFileVar filename = FileNameOf(..Files.MainFile) + ".anydata.h5";
            
            AnyOperationMacro Opr = {
            
            MacroStr = {
                ("classoperation Main.ArmStudy1.Output" + " " + strquote("Save data")
                + " --file=" + strquote(FilePathCompleteOf(.filename)) + " --type=Deep")
            };
            };
        };
        
        AnyProjectTaskOperation Load_Output_Data = {
            
            Description = {
            Title = "Loading output data from a previous simulation";
            BodyText = "This task load output saved by the task "
                        + strquote( AnyBodyLinkOf(&..Save_Output_Data) )
                        + " from file "
                        + strquote( strlink(.filename) );
            Tooltip = "Loading output data";
            //Files = .filename;
            };
            
            Operation = &Opr;
            
            AnyFileVar filename = .Save_Output_Data.filename;
            
            AnyOperationMacro Opr = {
            
            MacroStr = {
                "classoperation Main.ArmStudy1.Output" + " " + strquote("Load data")
                + " --file=" + strquote(FilePathCompleteOf(.filename))
            };
            };
            
        };
        
        ...
        
        };
        
        ...

    
Finally, a special task is demonstrated, namely AnyProjectTaskLoadModel.
It can load models and here, we shall indeed make an operation that
loads the model without any project definition. In other words, we
create an AnyProjectTaskLoadModel that loads the Demo.arm2d.any, but
without the AnyProject.any master file.
    
.. code-block:: AnyScriptDoc
    
    Main = {
    
    #include "Demo.arm2d.any"
    
    #include "DrawGroups.any"
    
    AnyProject ArmProject = {
        
        Tasks = {
    
        ...
        
        AnyProjectTaskLoadModel Load_the_model_without_project = {
            MainFile = "Demo.arm2d.any";
        };
        
        };

    ...
    


The practical relevance of this particular load task may be hard to see,
but it illustrates the option of loading another model from one already
loaded.

A more relevant case could have been to share the project source code
between two or more different Main file so that loading another Main
file would leave the project information, such as Tasks and Views, more
or less unaffected, even though the loaded model is shifted. This way a
Task flow that requires more than one model can in principle be bound
together in the same user interface.

HTML-based interaction in AnyProject
------------------------------------

From AnyBody version 5.1, the windows displaying AnyProject are now
capable of using HTML-based contents. This opens new possibilities for
user interaction with the model from AnyProject, and it also makes it
possible to have user-defined, dynamically updated, and nicely formatted
views in the AnyProject. In this section, we shall add simple examples
of both HTML-based and dynamically updated content as well as a
hyperlink for user interaction with the model to the AnyProject model we
have been creating above.

Adding HTML content to an AnyProject AnyDescription
---------------------------------------------------

We have already seen that the various types of AnyProject tasks all have
an AnyDescription member, which is used to describe the purpose and
functionality of the task. The AnyDescription can be used to display
HTML contents through two new optional member variables. We will start
by adding a new AnyProject task, which contains an AnyDescription with
some simple HTML. For this, we use the BodyHTML member, which is a
string-value object that is one option of entering the body text of the
description view.

Please add the following AnyProject task to the ``Tasks`` folder in the
example:

.. code-block:: AnyScriptDoc

    AnyProjectTaskOperation Set_value_example = {
    
        Description = {
            
            BodyHTML = "<b>Setting values in the model through AnyProject</b><br/><br/>"
                       +"This task demonstrates how we can use special AHTML links in HTML text to interact with a model in AnyBody";
            
        };
    
    };
    


After reloading the model and viewing the new AnyProject Task, we see
that the content of ``BodyHTML`` is now being used for displaying the
description of the task. When ``BodyHTML`` is defined in the script, it
will take precedence over any defined ``Title`` and ``BodyText`` in the
AnyDescription.

Please note that this AnyProject Task doesn’t actually have any
operation defined, and because of this, there is no “execute task”
button shown for it. In order to actually interact with the model from
this AnyProject task, we will be using some special HTML links, through
which we can pass commands to the AnyBody Modeling System.

Modify the newly created ``Set_value_example`` task to look like this:

.. code-block:: AnyScriptDoc

    AnyProjectTaskOperation Set_value_example = {
        
        Description = {
        BodyHTML = "<b>Setting values in the model through AnyProject</b><br/><br/>"
                    +"This task demonstrates how we can use special AHTML links in HTML text to interact with a model in AnyBody.<br/><br/>"
                    +"This link opens the <a href="+strquote()
                    +"Anybody -ob Main.ArmModel.Segs.LowerArm.HandNode"
                    +strquote()+">HandNode</a> in the modeltree.<br/>";
        };
    };
        
    

The new HTML link defined in the ``BodyHTML`` is formatted like this:

.. code-block:: html

    <a href="about:anybody -command argument">linktext</a>

The ``about:anybody`` (or just ``anybody``) beginning of the href-value
indicates to AnyBody that the link is an internal link and the *command
argument* tells what to do. In this case, we make a link to an object,
i.e., a link that takes us to the Model Tree of AMS.

Please note that in order to make the ``BodyHTML`` contain the quote
characters, we have to use the ``strquote()`` function to add “ to the
text string we create; we cannot enter quote characters directly, since
the AnyScript parser will see any second quote as the end of the entire
string leading to a syntax error for the rest of the string.

Next, we want to use another type of internal command link to actually
edit a value in the loaded model. The way we can do this is by using a
command for calling an AnyBody macro defined elsewhere in the AnyScript
code. We start by creating a new macro command.

Please modify the beginning of the AnyProject file to look like this:

.. code-block:: AnyScriptDoc

    Main = {
        
        #include "Demo.arm2d.any"
        
        #include "DrawGroups.any"
        
        AnyFolder Macros = {
        
        AnyStringVar SetValueSRel = ("classoperation Main.ArmModel.Segs.LowerArm.HandNode.sRel" 
                                     + " " + strquote("Set Value"));
        
        };
        ...
    


This adds a new ``Macros`` AnyFolder, which currently contains a single
string, defining a macro which calls the “Set Value” Class Operation on
the ``HandNode`` of the model. We now have to use this new string in our
AnyDescription ``BodyHTML``. We do this by adding a new HTML link to the
BodyHTML, where we use a special command argument that interprets and
executes this string as a macro.

Please modify the AnyProject Task from earlier to look like this:

.. code-block:: AnyScriptDoc

    AnyProjectTaskOperation Set_value_example = {
    
        Description = {
            BodyHTML = 
                " <b>Setting values in the model through AnyProject</b><br/><br/>"
                + "This task demonstrates how we can use special AHTML links in HTML text to interact with a model in AnyBody.<br/><br/>"
                + "This link opens the <a href="+strquote()
                + "about:Anybody -ob Main.ArmModel.Segs.LowerArm.HandNode"
                + strquote()+">HandNode</a> in the modeltree.<br/><br/>"
                + "This link calls the <a href="+strquote()
                + "about:Anybody -mc Main.Macros.SetValueSRel"
                + strquote()+">Set Value</a> class operation on the HandNode's sRel.<br/>";
        };
    };
    

For a full list of the available AHTML commands, please refer to the
AnyBody Reference Manual (Introduction->How to write AnyScript->Section:
HTML-based Descriptions).

Using external HTML files
-------------------------

We have seen that HTML content can be written directly in an
AnyDescription's ``BodyHTML`` member, but for larger HTML pages this can
become very cumbersome. It is therefore also possible to use external
HTML files as AnyDescription HTML sources. This is done by setting the
AnyDescription's ``HTMLURL`` member to the address of an external HTML
resource. This URL can point to a file in the local file system as well
as to a location on the Internet.

In this example, we will use an external HTML file to display a table
showing the ``r`` value of the ``Handnode`` and having the information
updated while an operation is being run on the model. We do this by
transferring the dynamic data to the external HTML file along with the
URL and then using JavaScript in the HTML file for inserting the data in
the right place. The data is transferred through the URL by encoding it
in the URL's query string.

We will use a previously prepared external HTML file called
:download:`AnyHTML_argument.htm <Downloads/AnyHTML_argument.htm>`.

We create a new AnyProject Task in the tasks folder for displaying this
HTML file and sending data to it:

.. code-block:: AnyScriptDoc

    AnyProjectTaskOperation Watch_value = {
    
        Description = {
            AnyFile filename = "AnyHTML_argument.htm";
            HTMLURL = 
                "file:///"+FilePathCompleteOf(filename)
                + "?name="+CompleteNameOf(Main.ArmModel.Segs.LowerArm.HandNode.r)
                + "&value="+strval(Main.ArmModel.Segs.LowerArm.HandNode.r[0],"%4g")
                + ", "+strval(Main.ArmModel.Segs.LowerArm.HandNode.r[1],"%4g")
                + ", "+strval(Main.ArmModel.Segs.LowerArm.HandNode.r[2],"%4g");
        };
    };
    

In this example we use the query-string of the URL to transfer both the
complete name and value to the HTML file. How we actually use the data
passed through the query-string is determined entirely by the contents
of the external HTML file.

Please also note that we use a local AnyFile variable to specify the
HTML file path without defining its absolute location in the script. The
AnyFile variable resolves the path of the AnyScript file, and we can get
the absolute file location through the ``FilePathCompleteOf`` function.
This is necessary because the ``HTMLURL`` has to be a complete absolute
URL and not a relative URL.

If we try loading the model now, we will see the HTML page, but it is
not being updated when we run the, for instance, InverseDynamics
operation in the model. This is because the AnyDescription containing
the ``HTMLURL`` is not part of the study, and therefore, the ``HTMLURL``
expression is not re-evaluated.

In order to enable this, we add the AnyDescription for this new task to
the ``ArmModelStudy`` by modifying the beginning of the AnyProject file to
look like this:

.. code-block:: AnyScriptDoc
    
    Main = {
    
        #include "Demo.arm2d.any"
        
        #include "DrawGroups.any"
        
        AnyFolder Macros = {
            AnyStringVar SetValueSRel = 
                ("classoperation Main.ArmModel.Segs.LowerArm.HandNode.sRel" + " "
                 + strquote("Set Value"));
        };
        
        ArmModelStudy={
            AnyFolder &ArmModelStudyUpdateHTMLURLarg = Main.ArmProject.Tasks.Watch_value.Description;
        };

        ...
    


If we reload the model and run the ``InverseDynamics`` operation now while
viewing the new AnyProject task, we will see that the displayed value
for ``r`` is being updated dynamically as the values change in the model.