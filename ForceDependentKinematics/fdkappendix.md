# Appendix: Cleaning and Preparing STL Surfaces for Contact Calculation

To use the AnyForceSurfaceContact, it is necessary that the STL- or
AnySurf-file fulfils some requirements to obtain good results.

- The surface should not have sharp edges in the region of contact.

  Sharp edges can cause a jump in calculation of the penetration
  depth of the two surfaces and thus can cause jumps in the contact
  force. For the FDK-solver, this is not easy to handle and can cause
  slow convergence or even failure.

- The surface should not have too large curvatures.

  Large curvatures on a surface cause, similar to sharp edges, lead
  to jumps in the calculation depth.

  On the master surface in a contact pairing (i.e. the surface for
  which distances for each vertex to the slave surface are
  calculated) big curvatures on the surface means big variations of
  the vertex normal, which are used to calculate the force direction.
  Thus, large curvatures causes can cause large variations in the
  force directions.

- The surface should not contain too small triangles.

  Small triangles, i.e. vertices which are too close to each other
  are collapsed into one vertex during the process of converting
  STL-files to AnySurf objects. Thus, too small triangles end up as
  degenerated triangles with edges of zero length and without area.
  These triangles must be ignored in the contact calculation and
  warnings show up.

- The face normal for each face of the surface should have a unique
  orientation.

  Make sure that the surface normal and the numbering of triangles
  (best counter clockwise for a consistent definition of the outer
  face normal) are consistent. The normal is used to define inside
  and outside of the surface and thus, which direction is
  penetration.

- To check the above mentioned requirements, you can use an external
  tool such as MeshLab (<https://www.meshlab.net/> ). To smooth
  sharp edges and large curvatures, filters, such as Laplacian
  filters, or others can be used, depending on the surface. Checking
  the face normals can be done by using the function Render->Show Face
  Normal.

  To delete small triangles in the surface, the following workflow can
  be used:

1. Load STL-file in MeshLab
2. Use Filters->Cleaning and Repairing->Merge Close Vertices. Use an abs
   tolerance bigger than 0.0001
3. Use Filters->Cleaning and Repairing->Remove Duplicate Faces
4. Use Filters->Cleaning and Repairing->Remove Duplicate
   Vertices
5. Use Filters->Cleaning and Repairing->Remove Zero Area Faces
