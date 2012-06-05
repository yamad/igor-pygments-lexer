
BUILTIN_FUNCTIONS = ["AddListItem", "AnnotationInfo", "AnnotationList", "AxisInfo",
                         "AxisList", "AxisValFromPixel", "BinarySearch", "BinarySearchInterp",
                         "CTabList", "CheckName", "CleanupName", "ContourInfo",
                         "ContourNameList", "ContourNameToWaveRef", "ContourZ",
                         "ControlNameList", "CountObjects", "CreationDate", "CsrWave",
                         "CsrWaveRef", "CsrXWave", "CsrXWaveRef", "DDEExecute", "DDEInitiate",
                         "DDEPokeString", "DDEPokeWave", "DDERequestString", "DDERequestWave",
                         "DDEStatus", "DDETerminate", "DataFolderDir", "DataFolderExists",
                         "DateTime", "DimDelta", "DimOffset", "DimSize", "FakeData",
                         "FindDimLabel", "FindListItem", "FontList", "FontSizeHeight",
                         "FontSizeStringWidth", "FunctionList", "GetDataFolder",
                         "GetDefaultFont", "GetDefaultFontSize", "GetDefaultFontStyle",
                         "GetDimLabel", "GetFormula", "GetIndexedObjName", "GetRTErrMessage",
                         "GetRTError", "GetRTStackInfo", "GetScrapText", "GetWavesDataFolder",
                         "GetWindow", "IgorInfo", "ImageInfo", "ImageNameList",
                         "ImageNameToWaveRef", "IndexedDir", "IndexedFile", "Inf",
                         "ItemsInList", "LayoutInfo", "LowerStr", "MacroList", "MatrixDet",
                         "MatrixDot", "MatrixRank", "MatrixTrace", "NVAR_Exists", "NaN",
                         "NameOfWave", "NumVarOrDefault", "NumberByKey", "ParamIsDefault",
                         "PICTInfo", "PICTList",
                         "PadString", "PathList", "Pi", "PossiblyQuoteName", "ProcedureText",
                         "RemoveByKey", "RemoveFromList", "RemoveListItem",
                         "ReplaceNumberByKey", "ReplaceStringByKey", "SVAR_Exists",
                         "ScreenResolution", "Secs2Date", "Secs2Time", "SelectNumber",
                         "SelectString", "SortList", "StrVarOrDefault", "StringByKey",
                         "StringFromList", "StringList", "StudentA", "StudentT", "TagVal",
                         "TagWaveRef", "TextFile", "TraceFromPixel", "TraceInfo",
                         "TraceNameList", "TraceNameToWaveRef", "UniqueName", "UpperStr",
                         "VariableList", "WaveDims", "WaveExists", "WaveInfo", "WaveList",
                         "WaveName", "WaveRefIndexed", "WaveType", "WaveUnits", "WhichListItem",
                         "WinList", "WinName", "WinRecreation", "WinType", "XWaveName",
                         "XWaveRefFromTrace", "abs", "acos", "acosh", "alog", "area", "areaXY",
                         "asin", "asinh", "atan", "atan2", "atanh", "bessI", "bessJ", "bessK",
                         "bessY", "betai", "binomial", "cabs", "ceil", "char2num", "cmplx",
                         "cmpstr", "conj", "cos", "cosh", "cpowi", "date", "date2secs", "deltax",
                         "e", "enoise", "erf", "erfc", "exists", "exp", "factorial", "faverage",
                         "faverageXY", "floor", "gammln", "gammp", "gammq", "gnoise", "hcsr", "i",
                         "ilim", "imag", "interp", "j", "jlim", "leftx", "limit", "ln", "log",
                         "magsqr", "max", "mean", "min", "mod", "modDate", "note", "num2char",
                         "num2istr", "num2str", "numpnts", "numtype", "p", "p2rect", "pcsr",
                         "pnt2x", "poly", "poly2D", "q", "qcsr", "r", "r2polar", "real", "rightx",
                         "round", "s", "sawtooth", "sign", "sin", "sinc", "sinh", "sqrt",
                         "startMSTimer", "stopMSTimer", "str2num", "stringmatch", "strlen",
                         "strsearch", "sum", "t", "tan", "tanh", "ticks", "time", "trunc", "vcsr",
                         "x", "x2pnt", "xcsr", "y", "z", "zcsr"]

BUILTIN_OPERATIONS = ["Abort", "AppendText", "AppendToGraph", "AppendToLayout",
                          "AppendToTable", "AppendXYZContour", "AutoPositionWindow",
                          "BackgroundInfo", "Beep", "BrowseURL", "BuildMenu", "Button", "Chart",
                          "CheckBox", "CheckDisplayed", "Close", "CloseMovie", "ColorScale",
                          "ColorTab2Wave", "ControlBar", "ControlInfo", "ControlNameList",
                          "ControlUpdate", "ConvexHull", "Convolve", "CopyScales", "Correlate",
                          "CtrlBackground", "CtrlFIFO", "Cursor", "CurveFit", "DefaultFont",
                          "DelayUpdate", "DeletePoints", "Differentiate", "Dir", "Display",
                          "DisplayHelpTopic", "DisplayProcedure", "DoAlert", "DoIgorMenu",
                          "DoUpdate", "DoWindow", "DoXOPIdle", "DrawLine", "DrawOval", "DrawPICT",
                          "DrawPoly", "DrawRRect", "DrawRect", "DrawText", "Duplicate",
                          "DuplicateDataFolder", "EdgeStats", "Edit", "ErrorBars", "Execute",
                          "Execute/P", "ExecuteScriptText", "FBinRead", "FBinWrite", "FFT",
                          "FIFO2Wave", "FIFOStatus", "FReadLine", "FSetPos", "FStatus",
                          "FTPDownload", "FTPUpload", "FastOp", "FindLevel", "FindLevels",
                          "FindPeak", "FindPointsInPoly", "FindRoots", "FindSequence",
                          "FindValue", "FuncFit", "FuncFitMD", "GetAxis", "GetMarquee",
                          "GetSelection", "GetWindow", "GraphNormal", "GraphWaveDraw",
                          "GraphWaveEdit", "GroupBox", "Hanning", "HideInfo", "HideProcedures",
                          "HideTools", "Histogram", "IFFT", "ImageAnalyzeParticles",
                          "ImageBlend", "ImageBoundaryToMask", "ImageEdgeDetection",
                          "ImageFileInfo", "ImageFilter", "ImageGenerateROIMask",
                          "ImageHistModification", "ImageHistogram", "ImageInfo",
                          "ImageInterpolate", "ImageLineProfile", "ImageLoad",
                          "ImageMorphology", "ImageNameList", "ImageNameToWaveRef",
                          "ImageRemoveBackground", "ImageRotate", "ImageSave", "ImageSeedFill",
                          "ImageStats", "ImageThreshold", "ImageTransform", "ImageWindow",
                          "IndexSort", "InsertPoints", "Integrate", "IntegrateODE",
                          "Interp3DPath", "KillBackground", "KillControl", "KillDataFolder",
                          "KillFIFO", "KillPICTs", "KillPath", "KillStrings", "KillVariables",
                          "KillWaves", "Label", "Layout", "Legend", "ListBox", "LoadData",
                          "LoadPICT", "LoadWave", "Make", "MakeIndex", "MarkPerfTestTime",
                          "MatrixConvolve", "MatrixEigenV", "MatrixFilter", "MatrixGaussJ",
                          "MatrixLLS", "MatrixLUBkSub", "MatrixLUD", "MatrixLinearSolve",
                          "MatrixMultiply", "MatrixSVBkSub", "MatrixSVD", "MatrixSchur",
                          "MatrixSolve", "MatrixTranspose", "Modify", "ModifyContour",
                          "ModifyGraph", "ModifyImage", "ModifyLayout", "ModifyPanel",
                          "ModifyTable", "ModifyWaterfall", "MoveDataFolder", "MoveString",
                          "MoveVariable", "MoveWave", "MoveWindow", "NewDataFolder", "NewFIFO",
                          "NewFIFOChan", "NewImage", "NewLayout", "NewMovie", "NewNotebook",
                          "NewPanel", "NewPath", "NewWaterfall", "Note", "Notebook", "Open",
                          "OpenNotebook", "OpenProc", "Optimize", "PathInfo", "PauseForUser",
                          "PauseUpdate", "PlayMovie", "PlayMovieAction", "PlaySnd", "PlaySound",
                          "PopupContextualMenu", "PopupMenu", "PopupMenuControl", "Preferences",
                          "Print", "PrintGraphs", "PrintLayout", "PrintNotebook", "Project",
                          "PulseStats", "PutScrapText", "Quit", "ReadVariables", "Redimension",
                          "Remove", "RemoveContour", "RemoveFromGraph", "RemoveFromLayout",
                          "RemoveFromTable", "RemoveImage", "RemoveLayoutObjects", "RemovePath",
                          "Rename", "RenameDataFolder", "RenamePICT", "RenamePath",
                          "ReorderTraces", "ReplaceText", "ReplaceWave", "ResumeUpdate",
                          "Rotate", "Save", "SaveExperiment", "SaveNotebook", "SavePICT",
                          "SetAxis", "SetBackground", "SetDashPattern", "SetDataFolder",
                          "SetDimLabel", "SetDrawEnv", "SetDrawLayer", "SetFormula",
                          "SetIgorMenuMode", "SetIgorOption", "SetMarquee", "SetProcessSleep",
                          "SetRandomSeed", "SetScale", "SetVariable", "SetWindow", "ShowInfo",
                          "ShowTools", "Silent", "Sleep", "Slider", "Slow", "Smooth",
                          "SmoothCustom", "Sort", "SoundInRecord", "SoundInSet",
                          "SoundInStartChart", "SoundInStatus", "SoundInStopChart",
                          "SphericalInterpolate", "SphericalTriangulate", "SplitString",
                          "Stack", "StackWindows", "String", "TabControl", "Tag", "TextBox", "Tile",
                          "TileWindows", "TitleBox", "Triangulate3d", "Unwrap", "ValDisplay",
                          "Variable", "WaveMeanStdv", "WaveStats", "boundingBall", "fprintf",
                          "popup", "printf", "sprintf", "sscanf", "wfprintf"]

