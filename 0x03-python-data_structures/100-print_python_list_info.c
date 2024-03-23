#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int Size = PyList_Size(p);
	int i;
	PyListObject *obj = (PyListObject *)p;

	printf("{*} size of the Python list = %li\n", size);
	printf("{*} Allocated = %li\n", obj->allocated);
	for (i = 0; < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
