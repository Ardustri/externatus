void main()
{
    import std.json;
    import std.stdio: write, writeln, writef, writefln;
    import std.conv : to;

    // parse a file or string of json into a usable structure
    string s = `{ "language": "D", "rating": 3.5, "code": "42" }`;
    JSONValue j = parseJSON(s);
    // j and j["language"] return JSONValue,
    // j["language"].str returns a string
    writeln(j["language"].str); // "D"
    writeln(j["rating"].floating); // 3.5

    // check a type
    long x;
    if (const(JSONValue)* code = "code" in j)
    {
        if (code.type() == JSONType.integer)
            x = code.integer;
        else
            x = to!int(code.str);
    }

    // create a json struct
    JSONValue jj = [ "language": "D" ];
    // rating doesnt exist yet, so use .object to assign
    jj.object["rating"] = JSONValue(3.5);
    // create an array to assign to list
    jj.object["list"] = JSONValue( ["a", "b", "c"] );
    // list already exists, so .object optional
    jj["list"].array ~= JSONValue("D");

    string jjStr = `{"language":"D","list":["a","b","c","D"],"rating":3.5}`;
    writeln(jj.toString); // jjStr
}
