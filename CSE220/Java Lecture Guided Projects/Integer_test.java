// Java program to illustrate
// various Integer methods
// Sourced from a website I don't remember the name of...
// (don't have patience to search for it again)
// This method is currently deprecated


public class Integer_test {
	public static void main(String args[])
	{
		int b = 55;
		String bb = "45";

		// Construct two Integer objects
		Integer x = new Integer(b);
		Integer y = new Integer(bb);

		// toString()
		System.out.println("toString(b) = " + Integer.toString(x));

		// toHexString(),toOctalString(),toBinaryString()
		// converts into hexadecimal, octal and binary
		// forms.
		System.out.println("toHexString(b) =" + Integer.toHexString(b));
		System.out.println("toOctalString(b) =" + Integer.toOctalString(b));
		System.out.println("toBinaryString(b) =" + Integer.toBinaryString(b));

		// valueOf(): return Integer object
		// an overloaded method takes radix as well.
		Integer z = Integer.valueOf(b);
		System.out.println("valueOf(b) = " + z);
		z = Integer.valueOf(bb);
		System.out.println("ValueOf(bb) = " + z);
		z = Integer.valueOf(bb, 6);
		System.out.println("ValueOf(bb,6) = " + z);

		// parseInt(): return primitive int value
		// an overloaded method takes radix as well
		int zz = Integer.parseInt(bb);
		System.out.println("parseInt(bb) = " + zz);
		zz = Integer.parseInt(bb, 6);
		System.out.println("parseInt(bb,6) = " + zz);

		// getInteger(): can be used to retrieve
		// int value of system property
		int prop = Integer.getInteger("sun.arch.data.model");
		System.out.println("getInteger(sun.arch.data.model) = " + prop);
		System.out.println("getInteger(abcd) ="	+ Integer.getInteger("abcd"));

		// an overloaded getInteger() method
		// which return default value if property not found.
		System.out.println("getInteger(abcd,10) =" + Integer.getInteger("abcd", 10));

		// decode() : decodes the hex,octal and decimal
		// string to corresponding int values.
		String decimal = "45";
		String octal = "005";
		String hex = "0x0f";

		Integer dec = Integer.decode(decimal);
		System.out.println("decode(45) = " + dec);
		dec = Integer.decode(octal);
		System.out.println("decode(005) = " + dec);
		dec = Integer.decode(hex);
		System.out.println("decode(0x0f) = " + dec);

		// rotateLeft and rotateRight can be used
		// to rotate bits by specified distance
		int valrot = 2;
		System.out.println("rotateLeft(0000 0000 0000 0010 , 2) =" + Integer.rotateLeft(valrot, 2));
		System.out.println("rotateRight(0000 0000 0000 0010,3) =" + Integer.rotateRight(valrot, 3));
	}
}

