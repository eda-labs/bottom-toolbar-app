# These are global status color buckets which overlays can use.  When displayed, these buckets will map to
# colors.  The specific colors may change from user to user so these buckets need to be defined more
# generically.
#
# First, there are 10 levels of good to bad where level 9 is the best and level 0 is the worst.  A common
# visualization would maybe map level 9 to green and level 0 to red.  Perhaps the other levels in between
# 9 and 0 use shades or dashed visualizations to indicate "not entirely good" or "not entirely bad".
# Think about a utilization overlay where you could have buckets for 0% to 10% utilized, 10% to 20% utilized,
# etc.
#
# Because overlays will commonly have binary or trinary states where things are either good/bad or
# maybe good/recovering/bad, we also define three constants for best, medium and worst which just map
# to the other buckets.
#
# Finally, we define 6 other arbitrary state buckets.  These are for states which are not inherently
# on a scale from good to bad.  Instead, each of these states are just independent of each other.  When
# visualized, we would tend to use distinct hues to tell them apart rather than some kind of gradation
# between them.
#
# Applications do not and should not try to use all of these states in their overlays.  Use what you
# need.  The UI will use the information it has to try to build a good color visualization at runtime
# based on the kind of statuses you say you will be returning.
DB_TOPO_COLOR_GOOD_BAD_9 = 'color_good_bad_9'
DB_TOPO_COLOR_GOOD_BAD_8 = 'color_good_bad_8'
DB_TOPO_COLOR_GOOD_BAD_7 = 'color_good_bad_7'
DB_TOPO_COLOR_GOOD_BAD_6 = 'color_good_bad_6'
DB_TOPO_COLOR_GOOD_BAD_5 = 'color_good_bad_5'
DB_TOPO_COLOR_GOOD_BAD_4 = 'color_good_bad_4'
DB_TOPO_COLOR_GOOD_BAD_3 = 'color_good_bad_3'
DB_TOPO_COLOR_GOOD_BAD_2 = 'color_good_bad_2'
DB_TOPO_COLOR_GOOD_BAD_1 = 'color_good_bad_1'
DB_TOPO_COLOR_GOOD_BAD_0 = 'color_good_bad_0'

DB_TOPO_COLOR_BEST = DB_TOPO_COLOR_GOOD_BAD_9
DB_TOPO_COLOR_MEDIUM = DB_TOPO_COLOR_GOOD_BAD_4
DB_TOPO_COLOR_WORST = DB_TOPO_COLOR_GOOD_BAD_0
DB_TOPO_COLOR_DEGRADED = DB_TOPO_COLOR_GOOD_BAD_1

DB_TOPO_COLOR_ARBITRARY_5 = 'color_arbitrary_5'
DB_TOPO_COLOR_ARBITRARY_4 = 'color_arbitrary_4'
DB_TOPO_COLOR_ARBITRARY_3 = 'color_arbitrary_3'
DB_TOPO_COLOR_ARBITRARY_2 = 'color_arbitrary_2'
DB_TOPO_COLOR_ARBITRARY_1 = 'color_arbitrary_1'
DB_TOPO_COLOR_ARBITRARY_0 = 'color_arbitrary_0'

DB_TOPO_COLOR_KPI_CRITICAL = 'kpi_critical'
DB_TOPO_COLOR_KPI_MAJOR = 'kpi_major'
DB_TOPO_COLOR_KPI_MINOR = 'kpi_minor'
DB_TOPO_COLOR_KPI_SUCCESS = 'kpi_success'
DB_TOPO_COLOR_KPI_WARNING = 'kpi_warning'
DB_TOPO_COLOR_KPI_CLEARED = 'kpi_cleared'
DB_TOPO_COLOR_KPI_MAINTENANCE = 'kpi_maintenance'
DB_TOPO_COLOR_KPI_INSTALLED = 'kpi_installed'
DB_TOPO_COLOR_KPI_INFO = 'kpi_info'
DB_TOPO_COLOR_KPI_INDETERMINATE = 'kpi_indeterminate'
DB_TOPO_COLOR_KPI_DISABLED = 'kpi_disabled'
DB_TOPO_COLOR_KPI_NEUTRAL = 'kpi_neutral'

DB_TOPO_COLOR_SEQUENTIAL_90 = 'sequential_90'
DB_TOPO_COLOR_SEQUENTIAL_80 = 'sequential_80'
DB_TOPO_COLOR_SEQUENTIAL_70 = 'sequential_70'
DB_TOPO_COLOR_SEQUENTIAL_60 = 'sequential_60'
DB_TOPO_COLOR_SEQUENTIAL_50 = 'sequential_50'
DB_TOPO_COLOR_SEQUENTIAL_40 = 'sequential_40'
DB_TOPO_COLOR_SEQUENTIAL_30 = 'sequential_30'
DB_TOPO_COLOR_SEQUENTIAL_20 = 'sequential_20'
DB_TOPO_COLOR_SEQUENTIAL_10 = 'sequential_10'
DB_TOPO_COLOR_SEQUENTIAL_00 = 'sequential_00'

DB_TOPO_TYPE_STRING = 'string'
DB_TOPO_TYPE_NUMBER = 'number'
DB_TOPO_TYPE_DATE = 'date'
DB_TOPO_TYPE_DATE_TIME = 'datetime'
DB_TOPO_TYPE_TIME = 'time'
DB_TOPO_TYPE_BOOLEAN = 'boolean'

DB_TOPO_ATTRIBUTES = 'attributes'
