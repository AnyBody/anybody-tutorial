---
substitutions:
  ModelView_Human_Adjusted: |-
    ```{image} _static/lesson2/image1.png
    ```
---

# Lesson 2: Adjusting the Human Model

The next step is to configure the anatomy of your human model. The body model is divided into individual
body parts: legs, arms, and trunk.

```{eval-rst}
.. todo:: Add a intersphinx link to AMMMR documentation on BM statments
```

:::{note}
Body model configuration refers to the selection of limb segments to include, muscle model types,
scaling algorithms etc. These are done by setting switches known as Body model (BM) parameters.
The configuration process is described in greater detail in this [document](https://anyscript.org/ammr-doc/bm_config/index)
:::

## Body model configuration

For this pedal model, you will configure the human model as follows:

- No muscles in the trunk segment.
- Both the left and the right arms will be excluded.
- The left leg segments will be excluded.
- There will be no muscles in the right leg.

This is implemented by declaring a number of `BM_*` configuraiton statements.

These can be included anywhere before the inclusion of the `HumanModel.any` file. But it is good practize to collect them in a single place so we will add them to the file `Model/BodyModelConfiguration.any`. 

```{code-block} AnyScriptDoc
---
emphasize-lines: 4
---
Main = {

  // Body Model configuration:
  #include "Model/BodyModelConfiguration.any"

```

Dobble click the line  `#include "Model/BodyModelConfiguration.any"` to quickly open the file.

Then add the BM configurations marked in red. 

```{code-block} AnyScriptDoc
#path __BM_PLUGIN_FILE__ "BodyModelConfiguration.any"
#define BM_CONFIG_PLUGIN __BM_PLUGIN_FILE__

// -----------------------------------------------------------------------------------
// The BodyModel configuration can be modified using BodyModel GUI plugin
// or by manually editing this file.
//
// Please see this this file for more information on the options:
// #path HTML_DOC "<AMMR_PATH_DOC>/bm_config/index.html"
// -----------------------------------------------------------------------------------

// Enable the TLEM2 lower extremity model
#define BM_LEG_MODEL _LEG_MODEL_TLEM2_


// Excluding the muscles in the trunk segments
§#define BM_TRUNK_MUSCLES OFF§
// Excluding the left arm segments
§#define BM_ARM_LEFT OFF§
// Excluding the right arm segments
§#define BM_ARM_RIGHT OFF§
// Excluding the left leg segments
§#define BM_LEG_LEFT OFF§
// Excluding the muscles in the right leg segments
§#define BM_LEG_MUSCLES_RIGHT OFF§

```

Loading the model (F7 key) should produce the following message:

```none
Model Warning: Study 'Main.Study' contains too few kinematic constraints to be kinematically determinate.
Evaluating model...
Loaded successfully.
Elapsed Time : 0.511000
```

The model view should show you the following picture:

{{ ModelView_Human_Adjusted }}

The message warns about the model containing too few kinematic
constraints, which means that AnyBody lacks the full information needed to perform movement.

This is because we are yet to specify how the human and environment are connected in this model.
This will be the topic of the next lesson.

