cxx = g++
cxxflags = -std=c++17 -Wall -c
lxxflags = -std=c++17
objects = Q1.o
target = Q1

$(target) : $(objects)
	$(cxx) $(lxxflags) $(objects) -o $(target)

$(objects) : Q1.cpp
	$(cxx) $(cxxflags) Q1.cpp

