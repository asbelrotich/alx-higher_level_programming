#include <Python.h>
#include <oblect.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int size = PyList_size(p);
	int i;
	PyListObject *obj = (PyListObject *)p;

	printf("{*} size of the Python list = %li\n", size);
	printf("{*} Allocated = %li\n", obj->allocated);
	for ( i = 0; < size; i++)
		printf("Element %i: %s\n", i, PY_TYPE(obj->ob_item[i])->tp_name);
}
