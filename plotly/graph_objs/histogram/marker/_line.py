from plotly.basedatatypes import BaseTraceHierarchyType


class Line(BaseTraceHierarchyType):

    # autocolorscale
    # --------------
    @property
    def autocolorscale(self):
        """
        Has an effect only if `marker.line.color` is set to a numerical
        array. Determines whether the colorscale is a default palette
        (`autocolorscale: true`) or the palette determined by
        `marker.line.colorscale`. In case `colorscale` is unspecified
        or `autocolorscale` is true, the default  palette will be
        chosen according to whether numbers in the `color` array are
        all positive, all negative or mixed.
    
        The 'autocolorscale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['autocolorscale']

    @autocolorscale.setter
    def autocolorscale(self, val):
        self['autocolorscale'] = val

    # cauto
    # -----
    @property
    def cauto(self):
        """
        Has an effect only if `marker.line.color` is set to a numerical
        array and `cmin`, `cmax` are set by the user. In this case, it
        controls whether the range of colors in `colorscale` is mapped
        to the range of values in the `color` array (`cauto: true`), or
        the `cmin`/`cmax` values (`cauto: false`). Defaults to `false`
        when `cmin`, `cmax` are set by the user.
    
        The 'cauto' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['cauto']

    @cauto.setter
    def cauto(self, val):
        self['cauto'] = val

    # cmax
    # ----
    @property
    def cmax(self):
        """
        Has an effect only if `marker.line.color` is set to a numerical
        array. Sets the upper bound of the color domain. Value should
        be associated to the `marker.line.color` array index, and if
        set, `marker.line.cmin` must be set as well.
    
        The 'cmax' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['cmax']

    @cmax.setter
    def cmax(self, val):
        self['cmax'] = val

    # cmin
    # ----
    @property
    def cmin(self):
        """
        Has an effect only if `marker.line.color` is set to a numerical
        array. Sets the lower bound of the color domain. Value should
        be associated to the `marker.line.color` array index, and if
        set, `marker.line.cmax` must be set as well.
    
        The 'cmin' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['cmin']

    @cmin.setter
    def cmin(self, val):
        self['cmin'] = val

    # color
    # -----
    @property
    def color(self):
        """
        Sets the marker.line color. It accepts either a specific color
        or an array of numbers that are mapped to the colorscale
        relative to the max and min values of the array or relative to
        `cmin` and `cmax` if set.
    
        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen
          - A number that will be interpreted as a color
            according to histogram.marker.line.colorscale
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self['color']

    @color.setter
    def color(self, val):
        self['color'] = val

    # colorscale
    # ----------
    @property
    def colorscale(self):
        """
        Sets the colorscale and only has an effect if
        `marker.line.color` is set to a numerical array. The colorscale
        must be an array containing arrays mapping a normalized value
        to an rgb, rgba, hex, hsl, hsv, or named color string. At
        minimum, a mapping for the lowest (0) and highest (1) values
        are required. For example, `[[0, 'rgb(0,0,255)', [1,
        'rgb(255,0,0)']]`. To control the bounds of the colorscale in
        color space, use `marker.line.cmin` and `marker.line.cmax`.
        Alternatively, `colorscale` may be a palette name string of the
        following list: Greys, YlGnBu, Greens, YlOrRd, Bluered, RdBu,
        Reds, Blues, Picnic, Rainbow, Portland, Jet, Hot, Blackbody,
        Earth, Electric, Viridis, Cividis
    
        The 'colorscale' property is a colorscale and may be
        specified as:
          - A list of 2-element lists where the first element is the
            normalized color level value (starting at 0 and ending at 1), 
            and the second item is a valid color string.
            (e.g. [[0, 'green'], [0.5, 'red'], [1.0, 'rgb(0, 0, 255)']])
          - One of the following named colorscales:
                ['Greys', 'YlGnBu', 'Greens', 'YlOrRd', 'Bluered', 'RdBu',
                'Reds', 'Blues', 'Picnic', 'Rainbow', 'Portland', 'Jet',
                'Hot', 'Blackbody', 'Earth', 'Electric', 'Viridis']

        Returns
        -------
        str
        """
        return self['colorscale']

    @colorscale.setter
    def colorscale(self, val):
        self['colorscale'] = val

    # colorsrc
    # --------
    @property
    def colorsrc(self):
        """
        Sets the source reference on plot.ly for  color .
    
        The 'colorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['colorsrc']

    @colorsrc.setter
    def colorsrc(self, val):
        self['colorsrc'] = val

    # reversescale
    # ------------
    @property
    def reversescale(self):
        """
        Has an effect only if `marker.line.color` is set to a numerical
        array. Reverses the color mapping if true (`cmin` will
        correspond to the last color in the array and `cmax` will
        correspond to the first color).
    
        The 'reversescale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['reversescale']

    @reversescale.setter
    def reversescale(self, val):
        self['reversescale'] = val

    # width
    # -----
    @property
    def width(self):
        """
        Sets the width (in px) of the lines bounding the marker points.
    
        The 'width' property is a number and may be specified as:
          - An int or float in the interval [0, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self['width']

    @width.setter
    def width(self, val):
        self['width'] = val

    # widthsrc
    # --------
    @property
    def widthsrc(self):
        """
        Sets the source reference on plot.ly for  width .
    
        The 'widthsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['widthsrc']

    @widthsrc.setter
    def widthsrc(self, val):
        self['widthsrc'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'histogram.marker'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        autocolorscale
            Has an effect only if `marker.line.color` is set to a
            numerical array. Determines whether the colorscale is a
            default palette (`autocolorscale: true`) or the palette
            determined by `marker.line.colorscale`. In case
            `colorscale` is unspecified or `autocolorscale` is
            true, the default  palette will be chosen according to
            whether numbers in the `color` array are all positive,
            all negative or mixed.
        cauto
            Has an effect only if `marker.line.color` is set to a
            numerical array and `cmin`, `cmax` are set by the user.
            In this case, it controls whether the range of colors
            in `colorscale` is mapped to the range of values in the
            `color` array (`cauto: true`), or the `cmin`/`cmax`
            values (`cauto: false`). Defaults to `false` when
            `cmin`, `cmax` are set by the user.
        cmax
            Has an effect only if `marker.line.color` is set to a
            numerical array. Sets the upper bound of the color
            domain. Value should be associated to the
            `marker.line.color` array index, and if set,
            `marker.line.cmin` must be set as well.
        cmin
            Has an effect only if `marker.line.color` is set to a
            numerical array. Sets the lower bound of the color
            domain. Value should be associated to the
            `marker.line.color` array index, and if set,
            `marker.line.cmax` must be set as well.
        color
            Sets the marker.line color. It accepts either a
            specific color or an array of numbers that are mapped
            to the colorscale relative to the max and min values of
            the array or relative to `cmin` and `cmax` if set.
        colorscale
            Sets the colorscale and only has an effect if
            `marker.line.color` is set to a numerical array. The
            colorscale must be an array containing arrays mapping a
            normalized value to an rgb, rgba, hex, hsl, hsv, or
            named color string. At minimum, a mapping for the
            lowest (0) and highest (1) values are required. For
            example, `[[0, 'rgb(0,0,255)', [1, 'rgb(255,0,0)']]`.
            To control the bounds of the colorscale in color space,
            use `marker.line.cmin` and `marker.line.cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys, YlGnBu, Greens,
            YlOrRd, Bluered, RdBu, Reds, Blues, Picnic, Rainbow,
            Portland, Jet, Hot, Blackbody, Earth, Electric,
            Viridis, Cividis
        colorsrc
            Sets the source reference on plot.ly for  color .
        reversescale
            Has an effect only if `marker.line.color` is set to a
            numerical array. Reverses the color mapping if true
            (`cmin` will correspond to the last color in the array
            and `cmax` will correspond to the first color).
        width
            Sets the width (in px) of the lines bounding the marker
            points.
        widthsrc
            Sets the source reference on plot.ly for  width .
        """

    def __init__(
        self,
        autocolorscale=None,
        cauto=None,
        cmax=None,
        cmin=None,
        color=None,
        colorscale=None,
        colorsrc=None,
        reversescale=None,
        width=None,
        widthsrc=None,
        **kwargs
    ):
        """
        Construct a new Line object
        
        Parameters
        ----------
        autocolorscale
            Has an effect only if `marker.line.color` is set to a
            numerical array. Determines whether the colorscale is a
            default palette (`autocolorscale: true`) or the palette
            determined by `marker.line.colorscale`. In case
            `colorscale` is unspecified or `autocolorscale` is
            true, the default  palette will be chosen according to
            whether numbers in the `color` array are all positive,
            all negative or mixed.
        cauto
            Has an effect only if `marker.line.color` is set to a
            numerical array and `cmin`, `cmax` are set by the user.
            In this case, it controls whether the range of colors
            in `colorscale` is mapped to the range of values in the
            `color` array (`cauto: true`), or the `cmin`/`cmax`
            values (`cauto: false`). Defaults to `false` when
            `cmin`, `cmax` are set by the user.
        cmax
            Has an effect only if `marker.line.color` is set to a
            numerical array. Sets the upper bound of the color
            domain. Value should be associated to the
            `marker.line.color` array index, and if set,
            `marker.line.cmin` must be set as well.
        cmin
            Has an effect only if `marker.line.color` is set to a
            numerical array. Sets the lower bound of the color
            domain. Value should be associated to the
            `marker.line.color` array index, and if set,
            `marker.line.cmax` must be set as well.
        color
            Sets the marker.line color. It accepts either a
            specific color or an array of numbers that are mapped
            to the colorscale relative to the max and min values of
            the array or relative to `cmin` and `cmax` if set.
        colorscale
            Sets the colorscale and only has an effect if
            `marker.line.color` is set to a numerical array. The
            colorscale must be an array containing arrays mapping a
            normalized value to an rgb, rgba, hex, hsl, hsv, or
            named color string. At minimum, a mapping for the
            lowest (0) and highest (1) values are required. For
            example, `[[0, 'rgb(0,0,255)', [1, 'rgb(255,0,0)']]`.
            To control the bounds of the colorscale in color space,
            use `marker.line.cmin` and `marker.line.cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys, YlGnBu, Greens,
            YlOrRd, Bluered, RdBu, Reds, Blues, Picnic, Rainbow,
            Portland, Jet, Hot, Blackbody, Earth, Electric,
            Viridis, Cividis
        colorsrc
            Sets the source reference on plot.ly for  color .
        reversescale
            Has an effect only if `marker.line.color` is set to a
            numerical array. Reverses the color mapping if true
            (`cmin` will correspond to the last color in the array
            and `cmax` will correspond to the first color).
        width
            Sets the width (in px) of the lines bounding the marker
            points.
        widthsrc
            Sets the source reference on plot.ly for  width .

        Returns
        -------
        Line
        """
        super(Line, self).__init__('line')

        # Import validators
        # -----------------
        from plotly.validators.histogram.marker import (line as v_line)

        # Initialize validators
        # ---------------------
        self._validators['autocolorscale'] = v_line.AutocolorscaleValidator()
        self._validators['cauto'] = v_line.CautoValidator()
        self._validators['cmax'] = v_line.CmaxValidator()
        self._validators['cmin'] = v_line.CminValidator()
        self._validators['color'] = v_line.ColorValidator()
        self._validators['colorscale'] = v_line.ColorscaleValidator()
        self._validators['colorsrc'] = v_line.ColorsrcValidator()
        self._validators['reversescale'] = v_line.ReversescaleValidator()
        self._validators['width'] = v_line.WidthValidator()
        self._validators['widthsrc'] = v_line.WidthsrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.autocolorscale = autocolorscale
        self.cauto = cauto
        self.cmax = cmax
        self.cmin = cmin
        self.color = color
        self.colorscale = colorscale
        self.colorsrc = colorsrc
        self.reversescale = reversescale
        self.width = width
        self.widthsrc = widthsrc

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)