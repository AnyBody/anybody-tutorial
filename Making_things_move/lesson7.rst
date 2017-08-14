Lesson 7: Troubleshooting C3D files
-----------------------------------

Occasionally you may experience problems reading C3D files and some of
the common issues are treated below. But before we get to them, let us
review a few facts about the C3D format. The C3D format is a public
domain, binary file format that has been used in Biomechanics, Animation
and Gait Analysis laboratories to record synchronized 3D and analog data
since the mid 1980's. It is supported by all major Motion Capture System
manufacturers, as well as other companies in the Biomechanics, Motion
Capture and Animation Industries, and there is a web site and community
devoted to its maintenance: `www.c3d.org <http://www.c3d.org/>`__.

The fact that the format is binary means that you cannot open a C3D file
and read it unless you have a special reader. There are readers
available at the c3d.org website, and most motion capture systems come
with software that reads and manipulates C3D files.

The fact that the file format is old and also designed to work on just
about every conceivable computer system means that it has a rather
complex structure and that there are rigid and precise rules for the
creation of C3D files. An unfortunate consequence of this is that the
format is error prone in the sense that not all software systems create
C3D files that live completely up to the standard. The AnyInputC3D class
in AnyBody is designed to cope with most of the common deviations from
the standard, but occasionally you may run into a problem. Here are some
of the common problems and solutions:

    I know my C3D file contains data, but I cannot see any markers
    moving anywhere in the Model View.

There are two usual causes for this problem. The first one is a scaling
issue. Data in C3D files is often in millimeters while standard settings
in AnyBody such as coordinate system sizes, marker sizes and such are
scaled to fit to a human-size model in meters. If AnyBody reads a file
in millimeters and interprets the result as meters, then the markers
will be very far apart, and if you Zoom All in the model view, the
markers may be so small compared to the viewed space that you cannot see
them.

The remedy is to set the PointScaleFactor in the AnyInputC3D object to
0.001, for instance, in the case of data in millimeters.

The second frequent explanation is that a C3D file contains two data
sections: one for raw data and one for processed data. By default,
AnyBody creates markers based on raw data, but if your C3D file has been
processed by other software prior to being read by AnyBody, then the
other software may have moved the marker data to the processed section
leaving you with nothing in your model.

The remedy is to set

.. code-block:: AnyScriptDoc

    MarkerUseAllPointsOnOff = On;


which instructs AnyBody to read data from both the raw and the processed
data sections.

    I get an error message when I load the model.

Many things can go wrong when loading a C3D file, simply because the
format of the file is relatively complex. The aim has been to make
AnyBody tolerant of some of the more usual deviations from the standard,
but sometimes things are irreparably wrong with the file and you will
end up with an error message that ideally should give you a hint of what
the problem is.

If you get an error message stating that the file cannot be opened, that
it is not a C3D file, or that the file is corrupt, then you likely have
to go back to your source and find out whether the data you have been
given has somehow been damaged.

Another class of error messages deal with specific problems with the
file, for instance that a required section or header is missing. This
can mean that AnyBody does not have the necessary information to process
the file and has to give up.

    The markers I get in my loaded model have different names from what
    I expected.

When you have loaded a C3D file into an AnyBody model, the object can
subsequently be browsed in the Model Tree in the left hand side of the
screen. Markers in C3D files have user-defined names for easier
identification, and sometimes you will find that the names you get in
the AnyBody Model Tree are not the same as you defined in your
experiment. There are two possible reasons for this:

The first reason is that AnyScript is a programming language and has
rules about allowed characters in names. So if the marker names in the
C3D file contain characters that have a special meaning, for instance
``*`` or ``+``, then they are automatically replaced by a text string of
the decimal ASCII code of the sign surrounded by underscores, for
instance ``_42_`` instead of ``*``.

The second possible reason is more subtle. The C3D standard has a
liberal length constraint (128 characters) on names of markers, but the
experimental community often uses strings of just four characters to
name markers, and this implicit convention has influenced some types of
software to truncate marker labels to four characters. So, if you have
named your markers ``MARKERRKNEE``, ``MARKERLKNEE``, ``MARKERSTERNUM`` and so
on, and your C3D file somewhere in the pipeline from experiment to
AnyBody passes through a piece of software that truncates the names,
then AnyBody will be given a C3D file where all the marker names are
truncated to just ``MARK``. AnyBody will not accept non-unique marker
names and therefore renames them automatically.