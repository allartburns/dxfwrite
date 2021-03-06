DXFEngine
=========

DXFEngine is the dxf entity creation factory, the dxfwrite interface.

.. class:: DXFEngine

    Factory, creates the dxf objects.

    This is the dedicated interface to dxfwrite, all table entries and all
    all DXF entities should be created by the methods of this object.
    All methods are static methods, so this object hasn't to be instantiated.

Drawing
-------

.. method:: DXFEngine.drawing(name='empty.dxf')

    Create a new drawing.

    The drawing-object contains all the sections, tables and entities, which
    are necessary for a valid dxf-drawing.

    For drawing methods see :class:`Drawing` class.

Table Entries
-------------

.. method:: DXFEngine.layer(name, **kwargs)
    :noindex:

    Create a new layer.

    :param str name: layer name
    :param int flags: standard flag values, bit-coded, default=0
    :param int color: color number, negative if layer is off, default=1
    :param str linetype: linetype name, default="CONTINUOUS"


.. seealso:: :ref:`Layer`

.. method:: DXFEngine.style(name, **kwargs)
    :noindex:

    Create a new textstyle.

    :param str name: textstyle name
    :param int flags: standard flag values, bit-coded, default=0
    :param int generation_flags: text generation flags, default = 0
    :param float height: fixed text height, 0 if not fixed = default
    :param last_height: last height used, default=1.
    :param float width: width factor, default=1.
    :param float oblique: oblique angle in degree, default=0.
    :param str font: primary font filename, default="ARIAL"
    :param str bigfont: big-font file name, default=""

.. seealso:: :ref:`Textstyle`

.. method:: DXFEngine.linetype(name, **kwargs)
    :noindex:

    Create a new linetype.

    :param str name: linetype name
    :param int flags: standard flag values, bit-coded, default=0
    :param str description: descriptive text for linetype, default=""
    :param pattern: line pattern definition, see method `DXFEngine.linepattern`

.. seealso:: :ref:`Linetype`

.. method:: DXFEngine.linepattern(pattern)
    :noindex:

    Create a :ref:`Linepattern` object from pattern-list.

    example linepattern([2.0, 1.25, -0.25, 0.25, -0.25]), for format
    description see object :ref:`Linepattern`.

.. method:: DXFEngine.view(name, **kwargs)
    :noindex:

    Create a new view.

    :param str name: view name
    :param int flags: standard flag values, bit-coded, default=0
        STD_FLAGS_PAPER_SPACE, if set this is a paper space view.
    :param float height, width: view height and width, in DCS?!, default=1.0
    :param center_point: view center point, in DCS?! (xy-tuple), default=(.5, .5)
    :param direction_point: view direction from target point, in WCS!!
        (xyz-tuple), default=(0, 0, 1)
    :param target_point: target point, in WCS!! (xyz-tuple), default=(0, 0, 0)
    :param float lens_length: lens length, default=50
    :param float front_clipping: front and back clipping planes,
        offsets from target point, default=0
    :param back_clipping: see front_clipping
    :param float view_twist: twist angle in degree, default=0
    :param int view_mode: view mode, bit-coded, default=0

.. method:: DXFEngine.vport(name, **kwargs)
    :noindex:

    Create a new viewport table entry.

    :param str name: viewport name
    :param int flags: standard flag values, bit-coded, default=0
    :param lower_left: lower-left corner of viewport, (xy-tuple), default=(0, 0)
    :param upper_right: upper-right corner of viewport, (xy-tuple), default=(1, 1)
    :param center_point: view center point, in WCS, (xy-tuple), default=(.5, .5)
    :param snap_base: snap base point, (xy-tuple), default=(0, 0)
    :param snap_spacing: snap spacing, X and Y (xy-tuple), default=(.1, .1)
    :param grid_spacing: grid spacing, X and Y (xy-tuple), default=(.1, .1)
    :param direction_point: view from direction point to target point (xyz-tuple), default=(0, 0, 1)
    :param target_point: view target point (xyz-tuple), default=(0, 0, 0)
    :param aspect_ratio: viewport aspect ratio (float), default=1.
    :param float lens_length: lens length, default=50
    :param float front_clipping: front and back clipping planes, offsets
        from target point , default=0
    :param float back_clipping: see front_clipping
    :param float view_twist: twist angle in degree, default=0
    :param float circle_zoom: circle zoom percent, default=100
    :param int view_mode: view mode, bit-coded, default=0
    :param int fast_zoom: fast zoom setting, default=1
    :param int ucs_icon: UCSICON settings, default=3
    :param int snap_on: snap on/off, default=0
    :param int grid_on: grid on/off, default=0
    :param int snap_style: snap style, default=0
    :param int snap_isopair: snap isopair, default=0

viewmode flags for `view` and `viewport`:

* VMODE_TURNED_OFF
* VMODE_PERSPECTIVE_VIEW_ACTIVE
* VMODE_FRONT_CLIPPING_ON
* VMODE_BACK_CLIPPING_ON
* VMODE_UCS_FOLLOW_MODE_ON
* VMODE_FRONT_CLIP_NOT_AT_EYE

.. method:: DXFEngine.ucs(name, **kwargs)
    :noindex:

    Create a new user-coordinate-system (UCS).

    :param str name: ucs name
    :param int flags: standard flag values, bit-coded
    :param origin: origin in WCS (xyz-tuple), default=(0, 0, 0)
    :param xaxis: xaxis direction in WCS (xyz-tuple), default=(1, 0, 0)
    :param yaxis: yaxis direction in WCS (xyz-tuple), default=(0, 1, 0)

.. method:: DXFEngine.appid(name)

DXF R12 Entities
----------------

.. method:: DXFEngine.arc(radius=1.0, center=(0., 0.), startangle=0., endangle=360., **kwargs)
    :noindex:

    Create a new arc-entity.

    :param float radius: arc radius
    :param center: center point (xy- or xyz-tuple), z-axis is 0 by default
    :param float startangle: start angle in degree
    :param float endangle: end angle in degree

.. seealso:: :ref:`ARC`

.. method:: DXFEngine.attdef(tag, insert=(0., 0.), **kwargs)
    :noindex:

    Create a new attribute definition, used in block-definitions.

    :param str text: attribute default text
    :param insert: insert point (xy- or xyz-tuple), z-axis is 0 by default
    :param str prompt: prompt text, like "insert a value:"
    :param str tag: attribute tag string
    :param int flags: attribute flags, bit-coded, default=0
    :param int length: field length ??? see dxf-documentation
    :param float height: textheight in drawing units (default=1)
    :param float rotation: text rotation (default=0) (all DXF angles in degrees)
    :param float oblique: text oblique angle in degree, default=0
    :param float xscale: width factor (default=1)
    :param str style: textstyle (default=STANDARD)
    :param int mirror: bit coded flags
    :param int halign: horizontal justification type, LEFT, CENTER, RIGHT,
        ALIGN, FIT, BASELINE_MIDDLE (default LEFT)
    :param int valign: vertical justification type, TOP, MIDDLE, BOTTOM,
        BASELINE (default BASELINE)
    :param alignpoint: align point (xy- or xyz-tuple), z-axis is 0 by
        default, if the justification is anything other than BASELINE/LEFT,
        alignpoint specify the alignment point (or the second alignment
        point for ALIGN or FIT).


.. seealso:: :ref:`ATTDEF`

.. method:: DXFEngine.attrib(text, insert=(0., 0.), **kwargs)
    :noindex:

    Create a new attribute, used in the entities section.

    :param str text: attribute text
    :param insert: insert point (xy- or xyz-tuple), z-axis is 0 by default
    :param str tag: attribute tag string
    :param int flags: attribute flags, bit-coded, default=0
    :param int length: field length ??? see dxf-documentation
    :param float height: textheight in drawing units (default=1)
    :param float rotation: text rotation (default=0) (all DXF angles in degrees)
    :param float oblique: text oblique angle in degree, default=0
    :param float xscale: width factor (default=1)
    :param str style: textstyle (default=STANDARD)
    :param int mirror: bit coded flags
    :param int halign: horizontal justification type, LEFT, CENTER, RIGHT,
        ALIGN, FIT, BASELINE_MIDDLE (default LEFT)
    :param int valign: vertical justification type, TOP, MIDDLE, BOTTOM,
        BASELINE (default BASELINE)
    :param alignpoint: align point (xy- or xyz-tuple), z-axis is 0 by
        default, if the justification is anything other than BASELINE/LEFT,
        alignpoint specify the alignment point (or the second alignment
        point for ALIGN or FIT).

.. seealso:: :ref:`ATTRIB`

.. method:: DXFEngine.block(name, basepoint=(0., 0.), **kwargs)
    :noindex:

    Create a block definition, for the blocks section.

    :param str name: blockname
    :param basepoint: block base point (xy- or xyz-tuple), z-axis is 0. by default
    :param int flags: block type flags
    :param str xref: xref pathname

.. seealso:: :ref:`BLOCK`

.. method:: DXFEngine.circle(radius=1.0, center=(0., 0.), **kwargs)
    :noindex:

    Create a new circle-entity.

    :param float radius: circle radius
    :param center: center point (xy- or xyz-tuple), z-axis is 0 by default

.. seealso:: :ref:`CIRCLE`

.. method:: DXFEngine.face3d(points=[], **kwargs)
    :noindex:

    Create a 3Dface entity with 3 or 4 sides of (3D) points, z-axis is 0
    by default.

    :param points: list of three or four 2D- or 3D-points
    :param int flags: edge flags, bit-coded, default=0


.. seealso:: :ref:`FACE3D`

.. method:: DXFEngine.insert(blockname, insert=(0., 0.), **kwargs)
    :noindex:

    Insert a new block-reference.

    :param str blockname: name of block definition
    :param insert: insert point (xy- or xyz-tuple), z-axis is 0 by default
    :param float xscale: x-scale factor, default=1.
    :param float yscale: y-scale factor, default=1.
    :param float zscale: z-scale factor, default=1.
    :param float rotation: rotation angle in degree, default=0.
    :param int columns: column count, default=1
    :param int rows: row count, default=1
    :param float colspacing: column spacing, default=0.
    :param float rowspacing: row spacing, default=0.

.. method:: DXFEngine.line(start=(0., 0.), end=(0., 0.), **kwargs)
    :noindex:

    Create a new line-entity of two (3D) points, z-axis is 0 by default.

    :param start: start point (xy- or xyz-tuple)
    :param end: end point (xy- or xyz-tuple)


.. seealso:: :ref:`LINE`

.. method:: DXFEngine.point(point=(0., 0.), **kwargs)
    :noindex:

    Create a new point-entity of one (3D) point, z-axis is 0 by default.

    :param point: start point (xy- or xyz-tuple)
    :param orientation: a 3D vector (xyz-tuple), orientation of PDMODE images ...
        see dxf documentation

.. seealso:: :ref:`POINT`

.. method:: DXFEngine.polyline(points=[], **kwargs)
    :noindex:

    Create a new polyline entity. Polymesh and polyface are also polylines.

    :param points: list of points, 2D or 3D points, z-value of 2D points is 0.
    :param polyline_elevation: polyline elevation (xyz-tuple), z-axis supplies
        elevation, x- and y-axis has to be 0.)
    :param int flags: polyline flags, bit-coded, default=0
    :param float startwidth: default starting width, default=0
    :param float endwidth: default ending width, default=0
    :param int mcount: polygon mesh M vertex count, default=0
    :param int ncount: polygon mesh N vertex count, default=0
    :param int msmooth_density: (if flags-bit POLYLINE_3D_POLYMESH is set)
        smooth surface M density, default=0
    :param int nsmooth_density: (if flags-bit POLYLINE_3D_POLYMESH is set)
        smooth surface N density, default=0
        same values as msmooth_density
    :param int smooth_surface: curves and smooth surface type, default=0
        ??? see dxf-documentation

.. seealso:: :ref:`POLYLINE`

.. method:: DXFEngine.polymesh(nrows, ncols, **kwargs)
    :noindex:

    Create a new polymesh entity.

    nrows and ncols >=2 and <= 256, greater meshes have to be divided into
    smaller meshes.

    The flags-bit `POLYLINE_3D_POLYMESH` is set.

    :param int nrows: count of vertices in m-direction, nrows >=2 and <= 256
    :param int ncols: count of vertices in n-direction, ncols >=2 and <= 256

.. seealso:: :ref:`POLYMESH`

.. method:: DXFEngine.polyface(precision=6, **kwargs)
    :noindex:

    Create a new polyface entity, polyface is a dxf-polyline entity!

    :param precision: vertex-coords will be rounded to precision places, and if
        the vertex is equal to an other vertex, only one vertex will be used,
        this reduces filespace, the coords will be rounded only for the
        comparison of the vertices, the output file has the full float
        resolution.

.. seealso:: :ref:`POLYFACE`

.. method:: DXFEngine.shape(name, insert=(0., 0.), **kwargs)
    :noindex:

    Insert a shape-reference.

    :param str name: name of shape
    :param insert: insert point (xy- or xyz-tuple), z-axis is 0 by default
    :param float xscale: x-scale factor, default=1.
    :param float rotation: rotation angle in degree, default=0
    :param float oblique: text oblique angle in degree, default=0

.. seealso:: :ref:`SHAPE`

.. method:: DXFEngine.solid(points=[], **kwargs)
    :noindex:

    Create a solid-entity by 3 or 4 vertices, the z-axis for 2D-points is 0.

    :param list points: three or four 2D- or 3D-points (tuples)

.. seealso:: :ref:`SOLID`

.. method:: DXFEngine.trace(points=[], **kwargs)
    :noindex:

    Create a trace-entity by 3 or 4 vertices, the z-axis for 2D-points is 0.

    :param points: list of three or four 2D- or 3D-points (tuples)

.. seealso:: :ref:`TRACE`

.. method:: DXFEngine.text(text, insert=(0., 0.), height=1.0, **kwargs)
    :noindex:

    Create a new text entity.

    :param str text: the text to display
    :param insert: insert point (xy- or xyz-tuple), z-axis is 0 by default
    :param float height: text height in drawing-units
    :param float rotation: text rotation in degree, default=0
    :param float xscale: text width factor, default=1
    :param float oblique: text oblique angle in degree, default=0
    :param str style: text style name, default=STANDARD
    :param int mirror: text generation flags, bit-coded, default=0
    :param int halign: horizontal justification type
    :param int valign: vertical justification type
    :param alignpoint: align point (xy- or xyz-tuple), z-axis is 0 by default
        If the justification is anything other than BASELINE/LEFT,
        alignpoint specify the alignment point (or the second alignment
        point for ALIGN or FIT).

    any combination of `valign` (TOP, MIDDLE, BOTTOM) and `halign` (LEFT,
    CENTER, RIGHT) is valid.

.. seealso:: :ref:`TEXT`

.. method:: DXFEngine.viewport(center_point, width, height, **kwargs)
    :noindex:

    Create a new viewport entity.

    :param center_point: center point of viewport in paper space as (x, y, z) tuple
    :param float width: width of viewport in paper space
    :param float height: height of viewport in paper space
    :param int status: 0 for viewport is off, >0 'stacking' order, 1 is highest priority
    :param view_target_point: as (x, y, z) tuple, default value is (0, 0, 0)
    :param view_direction_vector:  as (x, y, z) tuple, default value is (0, 0, 0)
    :param float view_twist_angle: in degrees, default value is 0
    :param float view_height: default value is 1
    :param view_center_point: as (x, y) tuple, default value is (0, 0)
    :param float perspective_lens_length:  default value is 50
    :param float front_clip_plane_z_value: default value is 0
    :param float back_clip_plane_z_value: default value is 0
    :param int view_mode: default value is 0
    :param int circle_zoom: default value is 100
    :param int fast_zoom: default value is 1
    :param int ucs_icon: default value is 3
    :param int snap: default value is 0
    :param int grid:  default value is 0
    :param int snap_style: default value is 0
    :param int snap_isopair: default value is 0
    :param float snap_angle: in degrees, default value is 0
    :param snap_base_point: as (x, y) tuple, default value is (0, 0)
    :param snap_spacing: as (x, y) tuple, default value is (0.1, 0.1)
    :param grid_spacing: as (x, y) tuple, default value is (0.1, 0.1)
    :param int hidden_plot: default value is 0

.. seealso::  :ref:`Viewport`

Composite Entities
------------------

.. method:: DXFEngine.mtext(text, insert, linespacing=1.5, **kwargs)
    :noindex:

    Create a multi-line text buildup `MText` with simple :ref:`TEXT`
    entities.

    Mostly the same kwargs like :ref:`TEXT`.

    .. caution::

           **alignpoint** is always the insert point, I don't need a
           second alignpoint because horizontal alignment FIT, ALIGN,
           BASELINE_MIDDLE is not supported.

    :param str text: the text to display
    :param insert: insert point (xy- or xyz-tuple), z-axis is 0 by default
    :param float linespacing: linespacing in percent of height, 1.5 = 150% =
        1+1/2 lines
    :param float height: text height in drawing-units
    :param float rotation: text rotion in dregree, default=0
    :param float xscale: text width factor, default=1
    :param float oblique: text oblique angle in degree, default=0
    :param str style: text style name, default=STANDARD
    :param int mirror: text generation flags, bit-coded, default=0
    :param int halign: horizontal justification type
    :param int valign: vertical justification type
    :param str layer: layer name
    :param int color: range [1..255], 0 = `BYBLOCK`, 256 = `BYLAYER`

    any combination of `valign` (TOP, MIDDLE, BOTTOM) and `halign` (LEFT,
    CENTER, RIGHT) is valid.


.. seealso:: :ref:`MText`

.. method:: DXFEngine.insert2(blockdef, insert=(0., 0.), attribs={}, **kwargs)
    :noindex:

    Insert a new block-reference with auto-creating of :ref:`ATTRIB` from
    :ref:`ATTDEF`, and setting attrib-text by the attribs-dict.
    (multi-insert is not supported)

    :param blockdef: the block definition itself
    :param insert: insert point (xy- or xyz-tuple), z-axis is 0 by default
    :param float xscale: x-scale factor, default=1.
    :param float yscale: y-scale factor, default=1.
    :param float zscale: z-scale factor, default=1.
    :param float rotation: rotation angle in degree, default=0.
    :param dict attribs: dict with tag:value pairs, to fill the the attdefs in the
        block-definition. example: {'TAG1': 'TextOfTAG1'}, create and insert
        an attrib from an attdef (with tag-value == 'TAG1'), and set
        text-value of the attrib to value 'TextOfTAG1'.
    :param str linetype: linetype name, if not defined = `BYLAYER`
    :param str layer: layer name
    :param int color: range [1..255], 0 = `BYBLOCK`, 256 = `BYLAYER`


.. seealso:: :ref:`Insert2`

.. method:: DXFEngine.table(insert, nrows, ncols, default_grid=True)
    :noindex:

    Table object like a HTML-Table, buildup with basic DXF R12 entities.

    Cells can contain Multiline-Text or DXF-BLOCKs, or you can create your own
    cell-type by extending the CustomCell object.

    Cells can span over columns and rows.

    Text cells can contain text with an arbitrary rotation angle, or letters can be
    stacked top-to-bottom.

    BlockCells contains block references (INSERT-entity) created from a block
    definition (BLOCK), if the block definition contains attribute definitions
    (ATTDEF-entity), attribs created by Attdef.new_attrib() will be added to the
    block reference (ATTRIB-entity).

    :param insert: insert point as 2D or 3D point
    :param int nrows: row count
    :param int ncols: column count
    :param bool default_grid: if `True` always a solid line grid will
        be drawn, if `False`, only explicit defined borders will be
        drawn, default grid has a priority of 50.

.. seealso:: :ref:`Table`

.. method:: DXFEngine.rectangle(insert, width, height, **kwargs)
    :noindex:

    2D Rectangle, build with a polyline and a solid as background filling

    :param point insert: where to place the rectangle
    :param float width: width in drawing units
    :param float height: height in drawing units
    :param float rotation: in degree (circle = 360 degree)
    :param int halign: `LEFT`, `CENTER`, `RIGHT`
    :param int valign: `TOP`, `MIDDLE`, `BOTTOM`
    :param int color: dxf color index, default is `BYLAYER`, if color is None, no
         polyline will be created, and the rectangle consist only of the
         background filling (if bgcolor != `None`)
    :param int bgcolor: dxf color index, default is `None` (no background filling)
    :param str layer: target layer, default is ``'0'``
    :param str linetype: linetype name, None = `BYLAYER`

.. seealso:: :ref:`Rectangle`

.. method:: DXFEngine.ellipse(center, rx, ry, startangle=0., endangle=360., rotation=0., segments=100, **kwargs)
    :noindex:

    Create a new ellipse-entity, curve shape is an approximation by :ref:`POLYLINE`.

    :param center: center point (xy- or xyz-tuple), z-axis is 0 by default
    :param float rx: radius in x-axis
    :param float ry: radius in y-axis
    :param float startangle: in degree
    :param float endangle: in degree
    :param float rotation: angle between x-axis and ellipse-main-axis in degree
    :param int segments: count of line segments for polyline approximation
    :param str linetype: linetype name, if not defined = `BYLAYER`
    :param str layer: layer name
    :param int color: range [1..255], 0 = `BYBLOCK`, 256 = `BYLAYER`

.. seealso:: :ref:`Ellipse`

.. method:: DXFEngine.spline(points, segments=100, **kwargs)
    :noindex:

    Create a new cubic-spline-entity, curve shape is an approximation by :ref:`POLYLINE`.

    :param points: breakpoints (knots) as 2D points (float-tuples), defines the
        curve, the curve goes through this points
    :param int segments: count of line segments for polyline approximation
    :param str linetype: linetype name, if not defined = `BYLAYER`
    :param str layer: layer name
    :param int color: range [1..255], 0 = `BYBLOCK`, 256 = `BYLAYER`

.. seealso:: :ref:`Spline`

.. method:: DXFEngine.bezier(**kwargs)
    :noindex:

    Create a new cubic-bezier-entity, curve shape is an approximation by :ref:`POLYLINE`.

    :param str linetype: linetype name, if not defined = `BYLAYER`
    :param str layer: layer name
    :param int color: range [1..255], 0 = `BYBLOCK`, 256 = `BYLAYER`


.. seealso:: :ref:`Bezier`

.. method:: DXFEngine.clothoid(start=(0, 0), rotation=0., length=1., paramA=1.0, mirror="", segments=100, **kwargs)
    :noindex:

    Create a new clothoid-entity, curve shape is an approximation by :ref:`POLYLINE`.

    :param start: insert point as 2D points (float-tuples)
    :param float rotation: in degrees
    :param loat length: length of curve in drawing units
    :param float paramA: clothoid parameter A
    :param str mirror: ``'x'`` for mirror curve about x-axis,
      ``'y'`` for mirror curve about y-axis,
      ``'xy'`` for mirror curve about x- and y-axis
    :param int segments: count of line segments for polyline approximation
    :param str linetype: linetype name, if not defined = `BYLAYER`
    :param str layer: layer name
    :param int color: range [1..255], 0 = `BYBLOCK`, 256 = `BYLAYER`

.. seealso:: :ref:`Clothoid`
