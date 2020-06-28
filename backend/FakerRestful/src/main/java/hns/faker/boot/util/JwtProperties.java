package hns.faker.boot.util;

public class JwtProperties {
    public static final String SECRET = "hnsfaker";
    public static final int EXPIRATION_TIME = 3600000; // 1h
    public static final String TOKEN_PREFIX = "Bearer ";
    public static final String HEADER_STRING = "Authorization";
}