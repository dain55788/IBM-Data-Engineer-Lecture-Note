from dataqualitychecks import check_for_nulls
from dataqualitychecks import check_for_min_max
from dataqualitychecks import check_for_valid_values
from dataqualitychecks import check_for_duplicates


test1={
	"testname":"Check for nulls",
	"test":check_for_nulls,
	"column": "billedamount",
	"table": "FactBilling"
}


test2={
	"testname":"Check for min and max",
	"test":check_for_min_max,
	"column": "month",
	"table": "DimMonth",
	"minimum":1,
	"maximum":12
}


test3={
	"testname":"Check for valid values",
	"test":check_for_valid_values,
	"column": "category",
	"table": "DimCustomer",
	"valid_values":{'Individual','Company'}
}


test4={
	"testname":"Check for duplicates",
	"test":check_for_duplicates,
	"column": "billid",
	"table": "FactBilling"
}

test5={
    "testname":"Check for nulls",
    "test":check_for_nulls,
    "column": "year",
    "table": "DimMonth"
}

test6={
    "testname":"Check for min and max",
    "test":check_for_min_max,
    "column": "quarter",
    "table": "DimMonth",
    "minimum":1,
    "maximum":4
}

test7={
    "testname":"Check for valid values",
    "test":check_for_valid_values,
    "column": "quarter",
    "table": "DimMonth",
    "valid_values":{1, 2, 3, 4}
}

test8={
    "testname":"Check for duplicates",
    "test":check_for_duplicates,
    "column": "customerid",
    "table": "DimCustomer"
}